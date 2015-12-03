"""
Creator: Chris Wagner
Created Date: 11/20/2015
Last Updated: 11/24/2015

Summary: 
    Dice Rolling Simulator is a program which takes a user-defined die sides and
    die quantity and outputs a random integer for each die.
"""

from sys import argv
from random import randrange

sides = -1
die_num = -1

try: 
    if len(argv) == 2:  
        sides = int(argv[1]) #If the die side value is input as an argv
        die_num = 1 #If the program is run with only one number, the program will automatically set die quantity = 1
    elif len(argv) == 3:
        sides = int(argv[1]) #If the die side value is input as an argv
        die_num = int(argv[2]) #Including the option to roll multiple dice at the same time 
    else:
        raise ValueError
    
    if sides <=0 or die_num <=0:
        print "One or both of your inputs are less than 1."
        raise ValueError
        
except ValueError:
    while type(sides) != int or type(die_num) != int or sides <= 0 or die_num <= 0: 
        print "Please input integers greater than 0."

        try:   ##'Try' blocks are processor intensive. Do not nest like this unless it is necessary! Programs like C++ and Java will take too much processor power with nested 'try' blocks.
               ##Python has a EAFP programming style - "Easier to ask for forgiveness than permission" (vs C++ which is a LBYL "Look Before You Leap" style)    
               ##Here the nested 'try' block should be fine since it is a small program with only 1 nesting.
            sides = int(raw_input("How many sides to each die? ")) #If the die side value is not input as an argv
            die_num = int(raw_input("How many dice do you want to roll? ")) #If the number of die value is not input as an argv

        except ValueError:
            pass #Will restart the while loop until the user inputs an integer

results = []
for item in range(1, die_num+1):
    results.append(randrange(1, sides+1))

die_dice = "die"
if die_num > 1:
    die_dice = "dice"
    
print "The outcome of rolling %s %s with %s sides is: %r" %(die_num, die_dice, sides, results)



'''
Testing Methodology:
1. python Dice Rolling Simulator.py 3 5     ---> Should roll 5 dice with 3 sides
2. python Dice Rolling Simulator.py 3       ---> Should roll 1 die  with 3 sides
3. python Dice Rolling Simulator.py         ---> Should prompt user for die count and die sides, then roll
4. python Dice Rolling Simulator.py 3 pie   ---> Should prompt user for die count and die sides, then roll
5. python Dice Rolling Simulator.py pie 5   ---> Should prompt user for die count and die sides, then roll
6. python Dice Rolling Simulator.py pie     ---> Should prompt user for die count and die sides, then roll
7. python Dice Rolling Simulator.py -1      ---> Should error, prompt user for die count and die sides, then roll
8. python Dice Rolling Simulator.py 3 -5    ---> Should error, prompt user for die count and die sides, then roll
9. python Dice Rolling Simulator.py (input negative or 0)      ---> Should error, prompt user for die count and die sides, then roll
10. python Dice Rolling Simulator.py 0, then input negative vals 2nd time      ---> Should error, prompt user for die count and die sides, error again, then roll
'''