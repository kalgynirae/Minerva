#!/usr/bin/python3

from probability import *

# Get invasion scenario. TODO add CLI arg-parsing
attackers = int(input("Enter the number of attackers: "))
defenders = int(input("Enter the number of defenders: "))
print()

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
    # TODO: add a/an distinction. Would this be worth the effort?
    print("The invasion has a %.2f%% chance of success." % (victory_prob * 100))
    
    # Receive a new command or scenario update. TODO: add histogram printing
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
