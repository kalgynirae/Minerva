"""
This module contains classes required to simulate the board game Risk.
"""

class Territory():
    """
    Simulates a territory on a Risk board
    """
    
    def __init__(self, name, continent=None, borders=None,
                     sea_lines=None, owner=None, armies=0):
        """
        Creates a new territory with the following attributes
        """
        
        self.name = name
        self.continent = continent
        self.borders = borders
        self.sea_lines = sea_lines
        self.owner = owner
        self.armies = armies

class Continent():
    """
    Simulates a continent, or group of territories, on a Risk board
    """
    
    def __init__(self, name, value, territories):
        """
        Creates a new continent
        """
        
        self.name = name
        self.value = value
        self.territories = territories

class Board():
    """
    Simulates a Risk board's territories and continents
    """
    
    def __init__(self, territories=None, continents=None):
        self.territories = territories
        self.continents = continents
    
    def __getitem__(self, key):
        #Return whatever territory/continent we find, if any
        return self.territories.get(key) or self.continents.get(key)
    
    def __setitem__(self, key, value):
        #Assign the item to the correct dictionary
        if isinstance(value, Territory):
            self.territories[key] = value
        elif isinstance(value, Continent):
            self.continents[key] = value

class StandardBoard(Board):
    """
    A standard Risk board
    """
    
    def __init__(self):
        #Set up all of the standard territories and continents
        self.territories = {}
        self.continents = {}
        
        #Make a list of territory names for setup
        names = [
        'Alaska',
        'Alberta',
        'Central America',
        'Eastern United States',
        'Greenland',
        'Northwest Territory',
        'Ontario',
        'Quebec',
        'Western United States',
        'Argentina',
        'Brazil',
        'Peru',
        'Venezuela',
        'Great Britain',
        'Iceland',
        'Northern Europe',
        'Scandinavia',
        'Southern Europe',
        'Ukraine',
        'Western Europe',
        'Congo',
        'East Africa',
        'Egypt',
        'Madagascar',
        'North Africa',
        'South Africa',
        'Afghanistan',
        'China',
        'India',
        'Irkutsk',
        'Japan',
        'Kamchatka',
        'Middle East',
        'Mongolia',
        'Siam',
        'Siberia',
        'Ural',
        'Yakutsk',
        'Eastern Australia',
        'Indonesia',
        'New Guinea',
        'Western Australia']
        
        #Create a territory for every name in the list
        for name in names:
            self[name] = Territory(name)
        
        #Now, we set up the continents
        #First, North America
        continent = []
        for n in names[0:9]:
            continent.append(self[n])
        
        self['North America'] = Continent('North America', 5, continent)
        
        #Next, South America
        continent = []
        for n in names[9:13]:
            continent.append(self[n])
        
        self['South America'] = Continent('South America', 2, continent)
        
        #Europe
        continent = []
        for n in names[13:20]:
            continent.append(self[n])
        
        self['Europe'] = Continent('Europe', 5, continent)
        
        #Africa
        continent = []
        for n in names[20:26]:
            continent.append(self[n])
        
        self['Africa'] = Continent('Africa', 3, continent)
        
        #Asia
        continent = []
        for n in names[26:38]:
            continent.append(self[n])
        
        self['Asia'] = Continent('Asia', 7, continent)
        
        #Australia/Oceania
        continent = []
        for n in names[38:42]:
            continent.append(self[n])
        
        self['Australia'] = Continent('Australia', 2, continent)
        
        #TO DO: Add borders and sea lines
