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

def calculate_battle(attackers, defenders, chance=1):
    """
    Accepts a battle scenario and returns the probabilties of possible outcomes
    after one round of battle using the table of casualty probabilities. The
    argument chance is the chance of the scenario provided in the arguments
    occurring in the first place.
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
        result = (attackers - p[0], defenders - p[1], p[2] * chance)
        results.append(result)
    
    #Return the results in a tuple (so that they're immutable)
    return tuple(results)

def calculate_invasion(attackers, defenders):
    """
    Accepts an invasion scenario (number of attackers & defenders) and returns
    the probabilities of all possible outcomes
    """
    #First, check if the arguments are both counting numbers
    if attackers < 1 or defenders < 1:
        return None
    
    if attackers % 1 != 0 or defenders % 1 != 0:
        return None
    
    #Create the initial scenario, the beginning of the battle, with a
    #probability of 1
    scenarios = [(attackers, defenders, 1)]
    
    #Initialize a dictionary to store the possible outcomes' probabilities
    outcomes = {}
    #For each scenario in which the attacker eliminates every defending army...
    for n in range(attackers):
        #...set the probability to 0 (we don't have any probability data yet)
        outcomes[(n+1, 0)] = 0
    
    #For each scenario in which the defender eliminates every attacking army...
    for n in range(defenders):
        #...set the probability to 0 (we don't have any probability data yet)
        outcomes[(0, n+1)] = 0
    
    #Loop through scenarios, calculating the results of a round of combat on
    #each scenario until they are all reduced to possible outcomes
    while scenarios:
        s = scenarios.pop() #Remove the last scenario from the list
        #Loop through its its possible outcomes after one round of combat
        for p in calculate_battle(*s):
            #If either the attacker or defender loses all their armies...
            if p[0] == 0 or p[1] == 0:
                #...add this scenario's probability to the outcomes dictionary
                outcomes[(p[0], p[1])] += p[2]
            #If the battle hasn't ended yet, add the new scenario to scenarios
            else: scenarios.append(p)
        
        scenarios.sort() #Sort the list now that it has new scenarios
        #Combine duplicate scenarios' probabilities in a new list
        i = 0
        while i < len(scenarios) - 1:
            cur = scenarios[i]
            nxt = scenarios[i+1]
            if cur[0] == nxt[0] and cur[1] == nxt[1]:
                scenarios[i] = (cur[0], cur[1], cur[2] + nxt[2])
                scenarios.pop(i+1)
            i += 1
    
    #Convert the outcomes to a list and return it
    new = []
    for key in sorted(outcomes):
        new.append((key[0], key[1], outcomes[key]))
    
    return tuple(new)
