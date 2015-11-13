#!/usr/bin/python3

"""
This module defines ui functions for the Risk program
"""

from probability import *

def print_scenario(attackers, defenders, a_min=0, d_min=0):
    # Display the current scenario, paying attention to grammatical details
    if attackers == 1:
        print("1 attacker vs. ", end='')
    else:
        print("%d attackers vs. " % attackers, end='')
    
    if defenders == 1:
        print("1 defender")
    else:
        print("%d defenders" % defenders)
    
    # Only print minimums if they're non-zero
    if a_min:
        print("The attacker wants to win with at least %d units." % a_min)
    
    if d_min:
        print("The attacker wants to reduce the defender to %d units." % d_min)

def print_odds(outcomes, a_min=0, d_min=0):
    # Add up the odds of all the outcomes favorable to the attacker
    victory_prob = 0
    for o in outcomes:
        if o[1] <= d_min:
            victory_prob += outcomes[o]
    
    # Print the chances of a successful invasion as a percentage
    percent = victory_prob * 100
    print("The invasion has a %.2f%% chance of success." % percent)

def interactive_mode(attackers, defenders, a_min=0, d_min=0):
    while attackers > a_min and defenders > d_min:
        # Print the current invasion scenario
        print_scenario(attackers, defenders, a_min, d_min)
        
        # Calculate and print the probabilities of the scenario's outcomes
        outcomes = calculate_invasion(attackers, defenders, a_min, d_min)
        print_odds(outcomes, a_min, d_min)
        
        # Receive a new command or scenario update.
        command = input("\n> ")
        
        if command == 'q': break
        
        # Determine how many armies will be eliminated this battle
        losses = min(attackers, defenders, 2)
        
        # Interpret the command and subtract armies appropriately
        # If the attacker won the battle, the defender loses armies
        if command == 'a':
            defenders -= losses
        # If the defender won the battle, the attacker loses armies
        elif command == 'd':
            attackers -= losses
        # If the battle was a tie, each loses one.
        elif command == 't' and losses == 2:
            attackers -= 1
            defenders -= 1
        # Tell the user if they messed up
        else:
            print("'%s' is not a valid command." % command)
    else:
        # If the invasion ended before the user quit, print the outcome
        if defenders > d_min:
            if defenders == 1:
                print("The defender has won with 1 army.")
            else:
                print("The defender has won with %d armies." % defenders)
        else:
            if attackers == 1:
                print("The attacker has won with 1 army.")
            else:
                print("The attacker has won with %d armies." % attackers)