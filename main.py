from prob import *

attackers = int(input("Enter the number of attackers: "))
defenders = int(input("Enter the number of defenders: "))

# Interactive loop
while attackers and defenders:
    # Display the new battle scenario
    print("%d attackers vs. %d defenders" % (attackers, defenders))
    
    # With the updated data, calculate and display new odds
    outcomes = calculate_invasion(attackers, defenders)
    
    victory_prob = 0
    for o in outcomes:
        if o[0]:
            victory_prob += outcomes[o]
    
    print("The attack has a %.2f%% chance of success." % (victory_prob * 100))
    
    command = input("> ")
    if command == 'q': break
    
    # Determine how many armies will be eliminated this battle
    losses = min(attackers, defenders, 2)
    # Interpret the command and subtract armies appropriately
    if command == 'a':
        defenders -= losses
    elif command == 'd':
        attackers -= losses
    elif command == 't' and losses == 2:
        attackers -= 1
        defenders -= 1
