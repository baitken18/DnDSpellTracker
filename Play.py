import pickle 
from Character import Character 
from Spellbook import Spellbook, Spell 

PATH_TO_CHARACTERS = 'c:/Users/baitk/Documents/D&D/Characters/'

def make_character(character_path = 'my_characters/'):
    '''
    Makes an instance of the character class via keyboard input.  
    Note that you will need a Spellbook object already prepared for this character.

    Parameters
    ----------
    character_path : str, optional
        The place where the character is saved.  This is not recommended to be changed.  By default is 'my_characters/'.
    '''
    name = input('Character Name: ')
    
    level = input('Starting Level: ')
    
    spellpath = input('Path to Spellbook/Spell Selection: ')
    with open(spellpath, 'rb') as f:
        spellbook = pickle.load(f) 
        
    character = Character(name, level, spellbook, None)
    with open(character_path + name + '.pickle') as f:
        pickle.dump(character, f) 
        
def play(character_name = None):
    if isinstance(character_name, type(None)):
        name = input('Character Name: ')
    with open(f'my_characters/{name}.pickle') as f:
        character = pickle.load(f) 

def open_character(name:str):
    with open(PATH_TO_CHARACTERS + f'{name}.pickle') as f:
        char = pickle.load(f)
    return char 

def main():
    print(PATH_TO_CHARACTERS)
    for i in range(0,21):
        print(f'{i} | {(i - 10)//2}')

if __name__ == '__main__':
    main()