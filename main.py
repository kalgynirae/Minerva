#!/usr/bin/python3

import argparse as ap
from ui import *

# First, handle argument parsing with the argparse module

# Create a new parser object, which we'll add the arguments to
parser = ap.ArgumentParser(description="Calculates probabilities for Risk")

# This function converts args to positive integers for troop numbers
def positive_int(string):
    """
    positive_int() converts args to positive integers for troop numbers
    """
    # Convert the argument string value to an integer
    try:
        value = int(string)
    except ValueError:
        # If it fails, raise an exception with an error message
        err_msg = "'%s' is not a positive integer" % string
        raise ap.ArgumentTypeError(err_msg)
    
    # If the integer conversion worked, make sure it's positive
    if value <= 0:
        # If not, raise an exception and tell the user
        err_msg = "'%d' is not a positive integer" % value
        raise ap.ArgumentTypeError(err_msg)
    
    return value

# Arguments for number of attackers and defenders
parser.add_argument("attackers", type=positive_int,
    help="number of attackers in the invasion scenario")

parser.add_argument("defenders", type=positive_int,
    help="number of defenders in the invasion scenario")

# Next, add arguments for attacker and defender minimums
parser.add_argument("-l", "--loss_value", type=positive_int, default=0,
    metavar="L",
    help="minimum number of troops the attacker would like to win with. Any "
         "outcomes in which the attacker's army size reaches or falls below "
         "this number before winning the invasion are counted as losses by "
         "the program.")

parser.add_argument("-w", "--win_value", type=positive_int, default=0,
    metavar="W",
    help="number of troops the attacker wishes to reduce the defending army "
         "to. Any outcomes in which the defender's army size reaches or "
         "falls below this number are counted as wins by the program.")

# Add the -i flag for interactive mode
parser.add_argument("-i", "--interactive", action="store_true",
    help="use interactive mode. The program will prompt the user for updates "
         "to the invasion, then outputs an updated probability of success.")

# Parse the arguments and extract all important data
options = parser.parse_args();

attackers = options.attackers
defenders = options.defenders

a_min = options.loss_value
d_min = options.win_value

interactive = options.interactive

# Make sure that the minimums are less than the troop numbers
# If so, print an error message and exit
if attackers <= a_min:
    error_msg = "the argument loss_value must be less than attackers"
    parser.error(error_msg)

if defenders <= d_min:
    error_msg = "the argument win_value must be less than defenders"
    parser.error(error_msg)

# Now that we've ensured the arguments are valid, let's use them!
# Do interactive mode if the user used the -i flag
if interactive:
    interactive_mode(attackers, defenders, a_min, d_min)
#Otherwise, just calculate and print the odds of success
else:
    odds = calculate_invasion(attackers, defenders, a_min, d_min)
    print_odds(odds)
