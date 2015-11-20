# Risk
This project is a tool to calculate probabilities of invasions in the board
game _Risk_. Not only can the tool output the exact probability of success for
a given attack, it can also calculate the probability of winning with a certain
number of troops left and/or wearing the enemy territory's forces down to a
specified number of units. It also has an interactive mode for reevaluating the
likelihood of an attack's success as it is underway.

##Installation
You will need Python 3 to use this tool. For now, there's no easy installation
method other than downloading the scripts and dropping them in /usr/local/bin.

##Usage
Here are some examples of all the tool's functionality.

###Basic Invasion Success Probability
The most basic function of the tool is calculating an attack's probability of
success.

Suppose the red player planned to invade a territory held by 5 blue units from a
territory containing 12. Because one unit must remain in the attacking country,
that leaves Red with an attacking force of 11. To find the likelihood of taking
Blue's territory, Red could run

```
$ ./main.py 11 5
The invasion has a 94.3% chance of success.
```

and immediately know his chances of victory.

###Including Retreats
As accurate as the probability given above is, it isn't very helpful.
Experienced _Risk_ players know that while *who* will win is usually easy to
determine, knowing *how many* troops they will win with is more difficult and
equally important.

In the above scenario, suppose that Red wants not only to take the territory
from Blue, but to hold it afterwards. Red thinks that 7 units are necessary for
this, and so will retreat if his attacking force (not including the one unit
remaining behind) reaches 7 before Blue's forces are eliminated. To find the
probability of taking the territory with at least 7 units, Red could do this:

```
$ ./main.py 11 5 -r 7
The invasion has a 50.7% chance of success.
```

In the above command, the -r option is the *retreat value*. This means that any
scenario in which the attacking force shrinks to 7 or less before eliminating
the defenders counts as a loss where the attacker retreats.

The program can also do the opposite. In a different scenario, suppose that
Green has 7 units in a territory. In an adjacent territory, Blue has a force of
5 units that Green wants to reduce to 2 so that Red, her ally, can conquer the
territory on his next turn. To find the odds of successfully wearing down the
Blue force to 2 or lower, Green can run this command:

```
$ ./main.py 6 5 -g 2
The invasion has a 80.0% chance of success.
```

Now Green knows that, if she's willing to sacrifice her entire attacking force,
she has an 80% chance of reducing Blue's force to only 2 units. The -g option,
the 2 in this command, is the *goal value* of the attack, another name for the
intended number of defenders at the attack's end.

Note that it's possible for Green to reduce Blue's force to 1 below the
goal value (in this case, 1) because 2 units are lost each round of combat.
These scenarios are included in the probability calculation, so if you intend
to reduce a territory's force without conquering it, use ```-g 2``` instead of
```-g 1```, which would include "accidentally" taking the territory as a 
successful outcome.
