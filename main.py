#!/usr/bin/python3

import argparse as ap
from probability import *

# First, handle argument parsing with the argparse module
parser = ap.ArgumentParser(description="Calculates probabilities for Risk")

# Arguments for number of attackers and defenders
parser.add_argument("attackers", type=int,
    help="number of attackers in the invasion scenario")

parser.add_argument("defenders", type=int,
    help="number of defenders in the invasion scenario")

# Next, add arguments for attacker and defender minimums
parser.add_argument("-l", "--loss_value", type=int, default=0, metavar="L",
    help="minimum number of troops the attacker would like to win with. Any "
         "outcomes in which the attacker's army size reaches or falls below "
         "this number are counted as losses by the program.")

parser.add_argument("-w", "--win_value", type=int, default=0, metavar="W",
    help="number of troops the attacker wishes to reduce the defending army "
         "to. Any outcomes in which the defender's army size reaches or "
         "falls below this number are counted as wins by the program.")

# Parse the arguments and extract all important data
# TODO add error checking for arguments
options = parser.parse_args();

attackers = options.attackers
defenders = options.defenders

a_min = options.L
d_min = options.W

# We'll default to interactive mode for now (still just testing)
# Have user input updates to invasion scenario and print updated probabilities
while attackers and defenders:
    # Display the current scenario, paying attention to grammatical details
    if attackers == 1:
        print("1 attacker vs. ", end='')
    else:
        print("%d attackers vs. " % attackers, end='')
    
    if defenders == 1:
        print("1 defender")
    else:
        print("%d defenders" % defenders)
    
    # Calculate the probabilities of the scenario
    outcomes = calculate_invasion(attackers, defenders)
    
    # Add up the odds of all the outcomes where the attacker has armies left
    victory_prob = 0
    for o in outcomes:
        if o[0]:
            victory_prob += outcomes[o]
    
    # Print the chances of a successful invasion as a percentage
    print("The invasion has a %.2f%% chance of success." % (victory_prob * 100))
    
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
else:
    # If the invasion ended before the user quit, print the outcome
    # Grammar is not fun
    if attackers:
        if attackers == 1:
            print("The attacker has won with 1 army.")
        else:
            print("The attacker has won with %d armies." % attackers)
    elif defenders:
        if defenders == 1:
            print("The defender has won with 1 army.")
        else:
            print("The defender has won with %d armies." % defenders)
