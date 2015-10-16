#!/usr/bin/python3
"""
This module defines functions used to calculate the odds of possible outcomes
in Risk battles, invasions, and campaigns.
"""

"""
casualty_odds is a table of possible casualty numbers and their probabilities
for the 6 possible battle scenarios
"""
casualty_odds = (
# Row for 1 attacker scenarios
(
    # 1 attacker, 1 defender
    ((0, 1, 5/12), # Attacker victory
    (1, 0, 7/12)), # Defender victory
    # 1 attacker, 2 defenders
    ((0, 1, 55/216), # Attacker victory
    (1, 0, 161/216)) # Defender victory
),
# Row for 2 attacker scenarios
(
    # 2 attackers, 1 defender
    ((0, 1, 125/216), # Attacker victory
    (1, 0, 91/216)), # Defender victory
    # 2 attackers, 2 defenders
    ((0, 2, 295/1296), # Attacker victory
    (2, 0, 581/1296), # Defender victory
    (1, 1, 420/1296)) # Tie
),
# Row for 3 attacker scenarios
(
    # 3 attackers, 1 defender
    ((0, 1, 855/1296), # Attacker victory
    (1, 0, 441/1296)), # Defender victory
    # 3 attackers, 2 defenders
    ((0, 2, 2890/7776), # Attacker victory
    (2, 0, 2275/7776), # Defender victory
    (1, 1, 2611/7776)) # Tie
)
)

# TODO: change calculate_battle to return a dictionary instead of a tuple
def calculate_battle(attackers, defenders, chance=1):
    """
    Accepts a battle scenario and returns the probabilties of possible outcomes
    after one round of battle using the table of casualty probabilities.
    """
    # First we check if either of the arguments are incorrect
    if attackers <= 0 or defenders <= 0:
        return None # I should replace this with more pythonic error handling
    
    #TODO add integer checks for arguments and a check for 0 < chance <= 1
    
    # Now that we're sure the arguments are valid, find the correct scenario
    # Assign the correct attacker number (according to the battle maximum)
    if attackers >= 3: a = 3
    else: a = attackers
    
    # Assign the correct defender number (according to the battle maximum)
    if defenders >= 2: d = 2
    else: d = 1
    
    # Include the external casualty table in the function
    global casualty_odds
    
    # Using the attacker and defender numbers, retrieve the casualty numbers
    casualty_possibilities = casualty_odds[a-1][d-1] # Subtract 1 for indexing
    
    # Apply these casualties to the arguments and return the probabilities
    results = []
    for p in casualty_possibilities:
        # chance is the chance of the given scenario happening at all
        result = (attackers - p[0], defenders - p[1], p[2] * chance)
        results.append(result)
    
    # Return the results in a tuple (so that they're immutable)
    return tuple(results)

def calculate_invasion(attackers, defenders):
    """
    A simple prototype for the calculate_invasion fundtion using the graph/
    table method.
    """
    
    # TODO: add parameter range checks (positive integers, etc.)
    
    # Create a grid of possible "states" of the invasion and their odds
    # These states are referenced with odds_grid[attackers][defenders]
    odds_grid = [[0 for y in range(defenders+1)] for x in range(attackers+1)]
    # Set the probability of the initial state of the invasion to 100%
    odds_grid[attackers][defenders] = 1
    
    # DEBUGGING
    for col in odds_grid: print(col)
    
    # Initialize the dictionary of outcomes and probabilities we'll return
    outcomes = {}
    
    # Loop through the grid, from the top-right to the lower-left, calculating
    # the probabilities of all possible states and outcomes of the battle.
    
    # First, go from the top-right grid-square up until the middle diagonal
    for distance in range(attackers):
        # Loop through a diagonal a certain distance from the top-right square
        for a, d in zip(range(attackers - distance, attackers+1), range(defenders, -1, -1)):
            # If the invasion's done, add probability to outcomes
            if a == 0 or d == 0:
                outcomes[(a, d)] = odds_grid[a][d]
                continue
            
            chance = odds_grid[a][d]
            
            # If the scenario's impossible, move on
            if chance == 0: continue
            
            # If not, calculate probabilities of states arising from this one
            for state in calculate_battle(a, d, chance):
                # Add the probability to the proper odds_grid position
                x = state[0]
                y = state[1]
                prob = state[2]
                
                odds_grid[x][y] += prob
    
    # Now continue from the middle diagonal down to the bottom-left grid-square
    for distance in range(defenders, -1, -1):
        # Loop through a diagonal of the grid, calculating probabilities
        for a, d in zip(range(attackers + 1), range(distance, -1, -1)):
            # If the invasion's done, add probability to outcomes
            if a == 0 or d == 0:
                outcomes[(a, d)] = odds_grid[a][d]
                continue
            
            chance = odds_grid[a][d]
            
            # If the scenario's impossible, move on
            if chance == 0: continue
            
            # If not, calculate probabilities of states arising from this one
            for state in calculate_battle(a, d, chance):
                # Add the probability to the proper odds_grid position
                x = state[0]
                y = state[1]
                prob = state[2]
                
                odds_grid[x][y] += prob
    
    # Finally, return the possible outcomes and their probabilities
    return outcomes
