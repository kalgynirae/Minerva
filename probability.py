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

def calculate_battle(attackers, defenders, chance=1):
    """
    Accepts a battle scenario and returns the probabilities of possible
    outcomes after one round of battle.
    """
    # Include the external casualty table in the function
    global casualty_odds
    
    # Set the number of dice to the maximum allowed for attacker and defender
    a = min(attackers, 3)
    d = min(defenders, 2)
    
    # Retrieve the possible troop losses for each side and their chances
    casualty_possibilities = casualty_odds[a-1][d-1] # Subtract 1 for indexing
    
    # Use possible troop losses to calculate possible outcomes
    outcomes = []
    for p in casualty_possibilities:
        result = (attackers - p[0], defenders - p[1], p[2] * chance)
        outcomes.append(result)
    
    # Return the outcomes in immutable, tuple form
    return tuple(outcomes)

def calculate_invasion(attackers, defenders, chance=1):
    """
    Accepts an invasion scenario (number of attackers and defenders) and its
    probability. Returns a dictionary of all possible outcomes and their
    probabilities.
    """
    # Create a grid of possible states of the invasion and their odds
    # These states are referenced using odds_grid[attackers][defenders]
    odds_grid = [[0 for y in range(defenders+1)] for x in range(attackers+1)]
    
    # Set the probability for the initial state (usually 100%)
    odds_grid[attackers][defenders] = chance
    
    # Initialize the dictionary of outcomes (keys) and probabilities (values)
    outcomes = {}
    
    # Loop through the grid, from the top-right to the lower-left, calculating
    # the probabilities of all possible states and outcomes of the battle.
    
    # First, go from the top-right grid-square up until the middle diagonal
    for dis in range(attackers):
        # Loop through a diagonal a certain distance from the top-right square
        diag = zip(range(attackers-dis, attackers+1), range(defenders, -1, -1))
        for a, d in diag:
            # Retrieve the probability of the current state
            chance = odds_grid[a][d]
            
            # If the current state's impossible, skip it
            if not chance: continue
            
            # If the current state is final, add its probability to outcomes
            if a == 0 or d == 0:
                outcomes[(a, d)] = chance
                continue
            
            # If not, calculate probabilities of states arising from this one
            for state in calculate_battle(a, d, chance):
                # Add the probability to the proper odds_grid position
                x = state[0]
                y = state[1]
                prob = state[2]
                
                odds_grid[x][y] += prob
    
    # Now continue from the middle diagonal down to the bottom-left grid-square
    for dis in range(defenders, -1, -1):
        # Loop through a diagonal a certain distance from the grid's lower-left
        diag = zip(range(attackers + 1), range(dis, -1, -1))
        for a, d in diag:
            # Retrieve the probability of the current state
            chance = odds_grid[a][d]
            
            # If the current state's impossible, skip it
            if not chance: continue
            
            # If the current state is final, add its probability to outcomes
            if a == 0 or d == 0:
                outcomes[(a, d)] = chance
                continue
            
            # If not, calculate probabilities of states arising from this one
            for state in calculate_battle(a, d, chance):
                # Add the probability to the proper odds_grid position
                x = state[0]
                y = state[1]
                prob = state[2]
                
                odds_grid[x][y] += prob
                
    
    # Finally, return the possible outcomes and their probabilities
    return outcomes
