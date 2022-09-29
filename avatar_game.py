from bender import Bender
from battle import Battle
import art
import random
from prettytable import PrettyTable

def create_battlers():
    benders = [
        Bender("Dragon",3,4,5,"Fire"),
        Bender("Moon",5,3,3,"Water"),
        Bender("Badger Mole",4,5,1,"Earth"),
        Bender("Sky Bison",5,1,4,"Air")
    ]
    return benders

def avatar_game():
    # Create benders
    benders = create_battlers()
    
    print("-"*50+ "\nWelcome to the Avatar Battler!\n"+ "-"*50)
    art.display_bender_art()
    stat_table = PrettyTable(['Bender', 'Element', 'Health', 'Attack', 'Speed'])
    for b in benders:
        stat_table.add_row([b.name, b.element, b.health, b.attack, b.speed])
    print(stat_table)

    player_bender = benders[int(input("Choose a Bender [0=Dragon, 1=Moon, 2=Badger Mole, 3=Sky Bison]: "))]
    computer_bender = benders[random.randint(0,3)]
    print("Computer chooses: "+computer_bender.name+"\n")
    # Create Battle
    b = Battle([player_bender, computer_bender])

    print(b)
    b.battle_animation()
    b.battle()

if __name__ == "__main__":
    avatar_game()