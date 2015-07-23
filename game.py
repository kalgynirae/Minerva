#!/usr/bin/python3
"""
This module contains classes required to simulate the board game Risk.
"""

class Territory():
    """
    Simulates a territory on a Risk board
    """
    
    def __init__(self, name, armies=0):
        """
        Creates a new territory with the following attributes
        """
        
        self.name = name
        self.armies = armies
        self.borders = []
        self.sea_lines = []
        self.continent = None
        self.owner = None
    
    #TODO: Add __repr__
    
    def __str__(self):
        return '"%s" %s %d' % (self.name, self.owner, self.armies)

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
    
    #TODO: Add __repr__ and __str__

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
    
    #TODO: Add __repr__ and __str__

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
        
        for n in names[0:9]:
            self[n].continent = self['North America']
        
        #Next, South America
        continent = []
        for n in names[9:13]:
            continent.append(self[n])
        
        self['South America'] = Continent('South America', 2, continent)
        
        for n in names[9:13]:
            self[n].continent = self['South America']
        
        #Europe
        continent = []
        for n in names[13:20]:
            continent.append(self[n])
        
        self['Europe'] = Continent('Europe', 5, continent)
        
        for n in names[13:20]:
            self[n].continent = self['Europe']
        
        #Africa
        continent = []
        for n in names[20:26]:
            continent.append(self[n])
        
        self['Africa'] = Continent('Africa', 3, continent)
        
        for n in names[20:26]:
            self[n].continent = self['Africa']
        
        #Asia
        continent = []
        for n in names[26:38]:
            continent.append(self[n])
        
        self['Asia'] = Continent('Asia', 7, continent)
        
        for n in names[26:38]:
            self[n].continent = self['Asia']
        
        #Australia/Oceania
        continent = []
        for n in names[38:42]:
            continent.append(self[n])
        
        self['Australia'] = Continent('Australia', 2, continent)
        
        for n in names[38:42]:
            self[n].continent = self['Australia']
        
        #Now we add the borders and sea lines connecting the territories
        borders = {
        'Alaska': ('Northwest Territory', 'Alberta'),
        'Alberta': ('Ontario', 'Western United States'),
        'Northwest Territory': ('Alberta', 'Ontario'),
        'Ontario': ('Western United States', 'Eastern United States', 'Quebec'),
        'Quebec': ('Eastern United States',),
        'Western United States': ('Eastern United States', 'Central America'),
        'Eastern United States': ('Central America',),
        'Central America': ('Venezuela',),
        'Venezuela': ('Peru', 'Brazil'),
        'Peru': ('Argentina', 'Brazil'),
        'Argentina': ('Brazil',),
        'Kamchatka': ('Yakutsk', 'Irkutsk', 'Mongolia'),
        'Yakutsk': ('Siberia', 'Irkutsk'),
        'Irkutsk': ('Siberia', 'Mongolia'),
        'Mongolia': ('Siberia', 'China'),
        'Siberia': ('Ural', 'China'),
        'Ural': ('Ukraine', 'Afghanistan', 'China'),
        'China': ('Afghanistan', 'India', 'Siam'),
        'India': ('Siam', 'Afghanistan', 'Middle East'),
        'Afghanistan': ('Ukraine', 'Middle East'),
        'Ukraine':
            ('Scandinavia', 'Northern Europe', 'Southern Europe', 'Middle East'),
        'Middle East': ('Southern Europe', 'Egypt'), 
        'Northern Europe': ('Western Europe', 'Southern Europe'),
        'Western Europe': ('Southern Europe', 'North Africa'),
        'Southern Europe': ('North Africa',),
        'North Africa': ('Egypt', 'East Africa', 'Congo'),
        'Egypt': ('East Africa',),
        'East Africa': ('Congo', 'South Africa'),
        'Congo': ('South Africa',),
        'Eastern Australia': ('Western Australia',)}
        
        #Add the borders to connect the territories
        for (territory, neighbors) in borders.items():
            for n in neighbors:
                #Add the border to both territories for movement between them
                self[territory].borders.append(self[n])
                self[n].borders.append(self[territory])
        
        sea_lines = {
        'Greenland': ('Northwest Territory', 'Ontario', 'Quebec', 'Iceland'),
        'Iceland': ('Great Britain', 'Scandinavia'),
        'Great Britain': ('Western Europe', 'Northern Europe', 'Scandinavia'),
        'Scandinavia': ('Northern Europe',),
        'Brazil': ('North Africa',),
        'Southern Europe': ('Egypt',),
        'East Africa': ('Middle East', 'Madagascar'),
        'Madagascar': ('South Africa',),
        'Kamchatka': ('Alaska', 'Japan'),
        'Japan': ('Mongolia',),
        'Indonesia': ('Siam', 'New Guinea', 'Western Australia'),
        'New Guinea': ('Western Australia', 'Eastern Australia')}
        
        #Add the sea lines to connect the territories
        for territory, neighbors in sea_lines.items():
            for n in neighbors:
                #Add the border to both territories for movement between them
                self[territory].sea_lines.append(self[n])
                self[n].sea_lines.append(self[territory])
