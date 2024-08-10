from Spellbook import Spellbook, Spell 
from dataclasses import dataclass
import StaticLookup as stat 
import pickle 

@dataclass
class Character:
    Name : str
    Level : int 
    spells : Spellbook
    #ability_score : int 
    prepared : list[Spell]
    
    def __post_init__(self):
        self.slots = stat.get_spell_slots(self.Level) 
        self.modifier = (self.Level - 10) // 2 
        self.proficiency = ((self.Level-1) // 4) + 2
        
    def level_up(self):
        self.Level += 1
        self.slots = stat.get_spell_slots(self.Level)
        
    def cast(self, spell:Spell, level = None):
        if level == None:
            self.slots[spell.Level - 1] -= 1
        elif level >= spell.Level:
            self.slots[level - 1] -= 1
        else:
            print(f'You cannot cast {spell.Name} at {level}')
        
    def take_long_rest(self):
        self.slots = stat.get_spell_slots(self.Level)
    
    def take_short_rest(self, recovery):
        for slot in recovery:
            self.slots[slot - 1] += 1
            
    def close(self):
        with open(f'my_characters/{self.name}.pickle') as f:
            pickle.dump(self, f)
    
if __name__ == '__main__':
    def _test_of_Character():
        b = Spellbook(['a','b','c'])
        c = Character('Fortan', 2, b, ['a'])
        print(c.Level)
        print(c.slots)
        c.level_up()
        print(c.Level)
        print(c.slots)

    _test_of_Character()