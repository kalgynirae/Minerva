#!/usr/bin/python3

import argparse as ap
from ui import *

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
         "this number before winning the invasion are counted as losses by "
         "the program.")

parser.add_argument("-w", "--win_value", type=int, default=0, metavar="W",
    help="number of troops the attacker wishes to reduce the defending army "
         "to. Any outcomes in which the defender's army size reaches or "
         "falls below this number are counted as wins by the program.")

# Parse the arguments and extract all important data
# TODO add error checking for arguments
options = parser.parse_args();

attackers = options.attackers
defenders = options.defenders

a_min = options.loss_value
d_min = options.win_value

# Just do interactive mode for now
interactive_mode(attackers, defenders, a_min, d_min)
