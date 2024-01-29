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

    def __str__(self) -> str:
        """Returning the value of the dice as a string."""
        return str(self.val)

    def win_or_loss(self, dice_guest: Dice) -> str:
        """Determine who's winning."""
        if self.val > dice_guest.val:
            return "win"
        elif self.val < dice_guest.val:
            return "lose"
        else:
            return "tie"

class RadNum:
    """Randomized Number used in the game."""
    val: int

    def __init__(self, input_upperrange: int) -> None:
        """Initial Constructor."""
        self.val = randint(1, input_upperrange)

#There're two different methods used for determining the players' wins and losses: dice or by random numbers.


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

    num_round: int = 1
    end_idc: bool = False
    guest_score: int = 0
    host_score: int = 0

    while end_idc == False:
        print()
        print()
        print(f"------Round {num_round}------")
        print(f"Let's start! {guest} first!")
        print(".............")
        dice_guest: Dice = Dice()
        print(f"{guest}, your dice rolls to {dice_guest} \n")
        
        print(f"{host} next!")
        print(".............")
        dice_host: Dice = Dice()
        print(f"{host}, your dice rolls to {dice_host} \n")

        print("The result is........")
        check: str = dice_host.win_or_loss(dice_guest)
        if  check == "win":
            print(f"{host} wins!")
            save_spend: str = input("Save it or Spend it? (Type in save or spend) ")
            print()
            if save_spend == "save":
                host_score += 1
            elif save_spend == "spend":
                print(f"{guest}, Truth or Dare!?")
        elif check == "lose":
            print(f"{guest} wins!")
            save_spend: str = input("Save it or Spend it? (Type in save or spend) ")
            print()
            if save_spend == "save":
                guest_score += 1
            elif save_spend == "spend":
                print(f"{host}, Truth or Dare!?")
        elif check == "tie":
            print("It's a tie!")
            print()

        print(f"{guest}: {guest_score}, {host}: {host_score} \n")

        end: str = input("Keep playing? (Type in yes or no) ")
        print()
        if end == "no":
            end_idc = True
        num_round += 1

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


# Introductions

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