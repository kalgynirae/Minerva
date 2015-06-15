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
		
		#I'm using the standard names for now, but I may change them
		#First, set up North America
		self['Alaska'] = Territory('Alaska')
		self['Alberta'] = Territory('Alberta')
		self['Central America'] = Territory('Central America')
		self['Eastern United States'] = Territory('Eastern United States')
		self['Greenland'] = Territory('Greenland')
		self['Northwest Territory'] = Territory('Northwest Territory')
		self['Ontario'] = Territory('Ontario')
		self['Quebec'] = Territory('Quebec')
		self['Western United States'] = Territory('Western United States')
		
		continent = (
		self['Alaska'],
		self['Alberta'],
		self['Central America'],
		self['Eastern United States'],
		self['Greenland'],
		self['Northwest Territory'],
		self['Ontario'],
		self['Quebec'],
		self['Western United States'])
		
		self['North America'] = Continent('North America', 5, continent)
		
		#Next, South America
		self['Argentina'] = Territory('Argentina')
		self['Brazil'] = Territory('Brazil')
		self['Peru'] = Territory('Peru')
		self['Venezuela'] = Territory('Venezuela')
		
		continent = (
		self['Argentina'],
		self['Brazil'],
		self['Peru'],
		self['Venezuela'])
		
		self['South America'] = Continent('South America', 2, continent)
		
		#Europe
		self['Great Britain'] = Territory('Great Britain')
		self['Iceland'] = Territory('Iceland')
		self['Northern Europe'] = Territory('Northern Europe')
		self['Scandinavia'] = Territory('Scandinavia')
		self['Southern Europe'] = Territory('Southern Europe')
		self['Ukraine'] = Territory('Ukraine')
		self['Western Europe'] = Territory('Western Europe')
		
		continent = (
		self['Great Britain'],
		self['Iceland'],
		self['Northern Europe'],
		self['Scandinavia'],
		self['Southern Europe'],
		self['Ukraine'],
		self['Western Europe'])
		
		self['Europe'] = Continent('Europe', 5, continent)
		
		#Africa
		self['Congo'] = Territory('Congo')
		self['East Africa'] = Territory('East Africa')
		self['Egypt'] = Territory('Egypt')
		self['Madagascar'] = Territory('Madagascar')
		self['North Africa'] = Territory('North Africa')
		self['South Africa'] = Territory('South Africa')
		
		continent = (
		self['Congo'],
		self['East Africa'],
		self['Egypt'],
		self['Madagascar'],
		self['North Africa'],
		self['South Africa'])
		
		self['Africa'] = Continent('Africa', 3, continent)
		
		#Asia
		self['Afghanistan'] = Territory('Afghanistan')
		self['China'] = Territory('China')
		self['India'] = Territory('India')
		self['Irkutsk'] = Territory('Irkutsk')
		self['Japan'] = Territory('Japan')
		self['Kamchatka'] = Territory('Kamchatka')
		self['Middle East'] = Territory('Middle East')
		self['Mongolia'] = Territory('Mongolia')
		self['Siam'] = Territory('Siam')
		self['Siberia'] = Territory('Siberia')
		self['Ural'] = Territory('Ural')
		self['Yakutsk'] = Territory('Yakutsk')
		
		continent = (
		self['Afghanistan'],
		self['China'],
		self['India'],
		self['Irkutsk'],
		self['Japan'],
		self['Kamchatka'],
		self['Middle East'],
		self['Mongolia'],
		self['Siam'],
		self['Siberia'],
		self['Ural'],
		self['Yakutsk'])
		
		self['Asia'] = Continent('Asia', 7, continent)
		
		#Australia/Oceania
		self['Eastern Australia'] = Territory('Eastern Australia')
		self['Indonesia'] = Territory('Indonesia')
		self['New Guinea'] = Territory('New Guinea')
		self['Western Australia'] = Territory('Western Australia')
		
		continent = (
		self['Eastern Australia'],
		self['Indonesia'],
		self['New Guinea'],
		self['Western Australia'])
		
		self['Australia'] = Continent('Australia', 2, continent)
		
		#Now we add the borders and sea lines to connect them
