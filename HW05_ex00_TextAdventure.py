#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(username, count=0):
    print username + " walk through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print username + ' takes the stairs'
        if (count > 0):
            print "but " + username + " is not happy about it"
        infinite_stairway_room(username,count + 1)
    #option 2 == "flee"
    if next == "flee":
        pass


def gold_room(username):
    print "This room is full of gold.  How much does " + username + " take?"

    next = raw_input("> ")
    try:
        how_much = int(next)
    except:
        dead("Man, learn to type a number.")
    else:
        if how_much < 50:
            print "Nice, " + username +" is not greedy, " + username + " wins!"
            exit(0)
        else:
            dead(username + " is a greedy bastard!")


def bear_room(username):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is " + username + " going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if ("take" in next) or ("honey" in next):   #here the user can also enter 'take the honey' or something similar
            dead("The bear looks at " + username + " then slaps his/her face off.")
        elif ("taunt" in next) and not bear_moved:    #here the user can also enter 'taunt the bear' or something similar
            print "The bear has moved from the door. " + username + " can go through it now."
            bear_moved = True
        elif ("taunt" in next) and bear_moved:     #here the user can also enter 'taunt the bear' or something similar
            dead("The bear gets pissed off and chews " + username + "'s leg off.")
        elif ("open" in next or "door" in next) and bear_moved:  #here the user can also enter 'open the door' or something similar
            gold_room(username)
        else:
            print "I got no idea what that means."


def cthulhu_room(username):
    print "Here " + username + " sees the great evil Cthulhu."
    print "He, it, whatever stares at " + username + " and " + username + " goes insane."
    print "Does " + username + " flee for his/her life or eat his/her head?"

    next = raw_input("> ")

    if "flee" in next:
        main
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(username)

def back_room(username):
    print "The room is filled with awkward programmers."
    print username + " states his/her name but nobody listens"
    print username + " starts programming python and never leaves"
    exit(0)

def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    username = sys.argv[1]

    print username + " is in a dark room."
    print "There is a door to " + username +"'s right and left."
    print "Which one does " + username + " take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    elif next == "back":
        back_room(username)
    elif next == "up":
        infinite_stairway_room(username,1)
    else:
        dead(username + "stumbles around the room until he starves.")

if __name__ == '__main__':
    main()
