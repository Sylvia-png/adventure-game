# Imports
import time
import random


# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
players = ["Bonnie", "adventure"]


# Functions
def print_pause(text):
    time.sleep(1)
    print(text)


# Introduction
def introduction():
    name = input("Hello adventure, what is your name?  \n")
    players[1] = name
    time.sleep(2)
    print_pause("Good, " + name + ". We are ready for the adventure!\n")
    print_pause("There are two children playing in the field with flowers and \
it is rumored that there is a dragon")
    print_pause("The boy named Thomas and a girl named Bonnie, they meet \
in a house of strangers")
    print_pause("Would be fun to play with them!\n")
    start_game(name)


# Start of game
def start_game(name):
    response = ""
    while response not in yes_no:
        response = input("Would you like to go to the cave?\nyes/no\n")
        if response == "yes":
            print_pause("Thomas says, no because it's dangerous!\n")
        elif response == "no":
            print_pause("You are not ready for this game. Goodbye, ")
            quit()
        else:
            print_pause("I didn't understand that.\n")
    next_part(name)


# Next part of game
def next_part(name):
    response = ""
    while response not in directions:
        print_pause("It is better to play with the children and in the \
toy house")
        print_pause("-If we go to the left, we see the living room")
        print_pause("-If we go to the right, we see the room.")
        print_pause("-Inside the house we see a box of spiders in front \
of us.")
        print_pause("-Behind you is the house exit.\n")
        response = input("What direction do you go?\
    \nleft/right/forward/backward\n")
        if response == "left":
            print_pause("We can watch TV, " + name + ".\n")
        elif response == "right":
            print_pause("We can play with a tent.\n")
        elif response == "forward":
            print_pause("It contains chocolates that we can eat.\n")
        elif response == "backward":
            print_pause("You leave the house. Goodbye, " + name + ".")
        else:
            print_pause("I didn't understand that.\n")
    hide_seek(name)


# End part of game
def hide_seek(name):
    response = ""
    while response not in yes_no:
        time.sleep(1)
        response = input("Hey," + name + " but wait a minute,\
what do you think if we play Hide-and-seek?\nyes/no\n")
        if response == "yes":
            print_pause("I will cover my eyes and when I start counting while \
everyone hides.\n")
            num = random.randint(1, 2)
            print_pause("I will start counting for " + str(num) + " minutes.")
            time.sleep(1)
            print("Ready I'm going to find you all.")
            i = 0
            while i < len(players):
                found = random.randint(1, 2)
                if found == 1:
                    print_pause("Thomas says: I found " + players[i] + "!")
                    print_pause("Player " + players[i] + " lost")
                else:
                    print_pause(players[i] + " says: safe!")
                    print_pause("player " + players[i] + " won")
                i += 1
            print_pause("Very good, hey I have to go now, bye see you soon!\n")
            new_game = input("Do you want to start a new game?\nyes/no\n")
            if new_game == "yes":
                introduction()
            else:
                print_pause("Ok good bye.")
                quit()
        elif response == "no":
            print_pause("you are not ready for this\
    game. Goodbye, " + name + ".")
            quit()
        else:
            print_pause("I didn't understand that.\n")


introduction()
