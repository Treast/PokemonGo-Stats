# PokemonGO-IV-Stats
Show all IV stats.

Example:
A perfect vaporeon will be show as "VAPOREON (CP XXX) : 100% (15/15/15)"

## Installation

### Requirements
- Python 2
- pip
- git

### Guide
```
git clone -b master https://github.com/Treast/PokemonGo-Stats.git
cd PokemonGo-Stats
pip install -r requirements.txt (Might need to sudo)
python2 main.py -a AUTH_SERVICE -u USERNAME -p PASSWORD -l LIMIT-IV
```

-a can be either 'ptc' or 'google'
-l is a percent. Pokemon with a smaller IV percent won't be shown.

### Example of usage
```
python2 main.py -a google -u pikachu@gmail.com -p ashsucks -l 80
```

## Credits
- [Boren](https://github.com/Boren/PokemonGO-IV-Renamer) for base script
- [tejado](https://github.com/tejado) for the API
- [PokemonGo-Bot People](https://github.com/PokemonGoF/PokemonGo-Bot) for some of the code
