from dataclasses import dataclass 

@dataclass(repr = False)
class Spell:
    Name : str
    Level : int 
    School : str 
    Save : str 
    Other_info : dict 
    Description : str
    
    def __repr__(self):
        return f'Name: {self.Name}\nLevel: {self.Level}\nSave: {self.Save}\nSchool: {self.School}\nDescription: {self.Description}'

@dataclass(repr=False)
class Spellbook:
    Spells : list[Spell]
    
    def __repr__(self):
        return '\n\n'.join([spell.__repr__() for spell in self.Spells])
    
    def add_spell(self, spell:Spell):
        if spell not in self.Spells:
            self.append(spell)
        else:
            print('That spell is already in your spellbook') 
    
    def remove_spell(self, spell:Spell):
        if spell in self.Spells:
            self.remove(spell)
        else:
            print('That spell was not in your spellbook') 
            
    def search_spells(self):
        #To be made
        #Will be able to provide SIMPLE filters to spellbook 
        pass 
    
    
    
    