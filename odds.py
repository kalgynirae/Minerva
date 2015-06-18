"""
This module defines functions used to calculate the odds of possible outcomes
in Risk battles, invasions, and campaigns.
"""

#This multidimensional tuple is a table of possible casualty numbers and their
#probabilities for the 6 possible battle scenarios

casualty_odds = (
#Row for 1 attacker scenarios
(
    #1 attacker, 1 defender
    ((0, 1, 5/12), #Attacker victory
    (1, 0, 7/12)), #Defender victory
    #1 attacker, 2 defenders
    ((0, 1, 55/216), #Attacker victory
    (1, 0, 161/216)) #Defender victory
),
#Row for 2 attacker scenarios
(
    #2 attackers, 1 defender
    ((0, 1, 125/216), #Attacker victory
    (1, 0, 91/216)), #Defender victory
    #2 attackers, 2 defenders
    ((0, 2, 295/1296), #Attacker victory
    (2, 0, 581/1296), #Defender victory
    (1, 1, 420/1296)) #Tie
),
#Row for 3 attacker scenarios
(
    #3 attackers, 1 defender
    ((0, 1, 855/1296), #Attacker victory
    (1, 0, 441/1296)), #Defender victory
    #3 attackers, 2 defenders
    ((0, 2, 2890/7776), #Attacker victory
    (2, 0, 2275/7776), #Defender victory
    (1, 1, 2611/7776)) #Tie
)
)

def calculate_battle(attackers, defenders):
    """
    Accepts a battle scenario and returns the probabilties of possible outcomes
    after one round of battle using the table of casualty probabilities
    """
    #First we check if either of the arguments are incorrect
    if attackers <= 0 or defenders <= 0:
        return None #I should replace this with more pythonic error handling
    
    #Now that we're sure the arguments are valid, find the correct scenario
    #Assign the correct attacker number (according to the battle maximum)
    if attackers >= 3: a = 3
    else: a = attackers
    
    #Assign the correct defender number (according to the battle maximum)
    if defenders >= 2: d = 2
    else: d = 1
    
    #Include the external casualty table in the function
    global casualty_odds
    
    #Using the attacker and defender numbers, retrieve the casualty numbers
    casualty_possibilities = casualty_odds[a-1][d-1] #Subtract 1 for indexing
    
    #Apply these casualties to the arguments and return the probabilities
    results = []
    for p in casualty_possibilities:
        result = (attackers - p[0], defenders - p[1], p[2])
        results.append(result)
    
    return tuple(results)
