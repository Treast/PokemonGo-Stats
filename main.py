#!/usr/bin/env python

import json
import time
import argparse
from sets import Set
from pgoapi import PGoApi

class Renamer():

    def init_config(self):
        parser = argparse.ArgumentParser()
    
        parser.add_argument("-a", "--auth_service")
        parser.add_argument("-u", "--username")
        parser.add_argument("-p", "--password")
        parser.add_argument("-l", "--limit")
        parser.add_argument("--clear", action = 'store_true', default = False)

        self.config = parser.parse_args()
        self.config.delay = 2

    def start(self):
        print("Start Stats")
        self.pokemon_list = json.load(open('pokemon.json'))
        self.init_config()
        self.setup_api()
        self.get_pokemons()
        self.calc_iv()
        self.pokemons.sort(key=lambda x: x['iv'])
        self.show_stats()

    def setup_api(self):
        self.api = PGoApi()

        if not self.api.login(self.config.auth_service, str(self.config.username), str(self.config.password)):
            print("Login error")
            exit(0)

        print("Signed in")

    def get_pokemons(self):
        print("Getting pokemon list")
        self.api.get_inventory()
        response_dict = self.api.call()

        self.pokemons = []

        for item in response_dict['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']:
            try:
                reduce(dict.__getitem__, ["inventory_item_data", "pokemon_data"], item)
            except KeyError:
                pass
            else:
                try:
                    pokemon = item['inventory_item_data']['pokemon_data']

                    pid = pokemon['id']
                    num = int(pokemon['pokemon_id']) - 1
                    name = self.pokemon_list[int(num)]['Name']
                    
                    attack = pokemon.get('individual_attack', 0)
                    defense = pokemon.get('individual_defense', 0)
                    stamina = pokemon.get('individual_stamina', 0)
                    nickname = pokemon.get('nickname', 'NONE')
                    cp = pokemon.get('cp', 0)

                    self.pokemons.append({
                        'id': pid,
                        'name': name,
                        'nickname': nickname,
                        'num': num,
                        'cp': cp,
                        'attack': attack,
                        'defense': defense,
                        'stamina': stamina,
                        'iv': 0,
                    })
                except:
                    pass


    def calc_iv(self):
        for pokemon in self.pokemons:
            pokemon['iv'] = pokemon['attack'] + pokemon['defense'] + pokemon['stamina']      
    
    def show_stats(self):      
        for pokemon in self.pokemons:
            if pokemon['iv'] >= (int(self.config.limit)*45)/100:
                print pokemon['name'].upper() + " CP(" + str(pokemon['cp']) + ") " + str(int((pokemon['iv']*100)/45)) + "% (" + str(pokemon['attack']) + "/" + str(pokemon['defense']) + "/" + str(pokemon['stamina']) + ")"



if __name__ == '__main__':
    Renamer().start()
