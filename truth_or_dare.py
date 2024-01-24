"""Truth or Dare"""

from __future__ import annotations
from random import randint
from typing import Union

class Dice:
    """Dice(s) used in the game."""
    val: int

    def __init__(self) -> None:
        """Initial constructor."""
        self.val = randint(1, 6)

    def __add__(self, rhs: Union[float, Dice]) -> int:
        """Adding two dices."""
        result: int = 0
        if type(rhs) == float:
            self.val += rhs
        else:
            self.val += rhs.val
        result = self.val 

def game_m1(host: str, guest: str) -> str:
    """Mode 1: Throwing the dice one by one."""
    print(f"Hi {host} and {guest}!")
    print("Below are the rules for this gameeeeeeeee!")

    check: str = ""
    idx_rules: int = 0
    while (check != "yes") and idx_rules < 5:
        print("Rule 1: ")
        print("Rule 2: ")
        check = input("Are u ready?? If you do, type in yes: ")
        idx_rules += 1
    if idx_rules == 5:
        print("Five times? Seriously? This game is not for idoits!")
        quit()

    return(f"See u next time! {host} and {guest}")


def game_m2(host: str, guest: str):
    """Mode 2: Using the sum of 5 rolls"""
   
    print(f"Hi {host} and {guest}!")
    print("Below are the rules for this gameeeeeeeee!")

    check: str = ""
    idx_rules: int = 0
    while (check != "yes") and idx_rules < 5:
        print("Rule 1: ")
        print("Rule 2: ")
        check = input("Are u ready?? If you do, type in yes: ")
        idx_rules += 1
    if idx_rules == 5:
        print("Five times? Seriously? This game is not for idoits!")
        quit()

    return(f"See u next time! {host} and {guest}")


def game_m3(host: str, guest: str):
    """Mode 3: 10 rolls at a time"""
    
    print(f"Hi {host} and {guest}!")
    print("Below are the rules for this gameeeeeeeee!")

    check: str = ""
    idx_rules: int = 0
    while (check != "yes") and idx_rules < 5:
        print("Rule 1: ")
        print("Rule 2: ")
        check = input("Are u ready?? If you do, type in yes: ")
        idx_rules += 1
    if idx_rules == 5:
        print("Five times? Seriously? This game is not for idoits!")
        quit()

    return(f"See u next time! {host} and {guest}")


print("Welcomeeeeeeeeee")
player_1: str = input("What's your name? ")
player_2: str = input("What's your opponent's name? ")
#Greeting to the players and Collect their names

print("Great! There're three game modes that you can choose:")
print("Mode 1: one by one; Mode 2: sum of 5 rolls; Mode 3: 10 rolls at a time")
game_mode = input("Which mode do u wanna play (Type in a number)? ")
#gamemode selection

idx_gameentry: int = 0
while (type(game_mode) != int) and (len(game_mode) != 1):
    game_mode = input("That's incorrect! Use the correct format! Try again: ")
    idx_gameentry += 1
    if idx_gameentry > 9:
        print("Stop playing with me! Access denied!")
        quit()
#Determining whether the input of game_mode is correct

if int(game_mode) == 1:
    print(game_m1(player_1, player_2))

if int(game_mode) == 2:
    print(game_m2(player_1, player_2))

if int(game_mode) == 3:
    print(game_m3(player_1, player_2))

#Entering the correct game mode