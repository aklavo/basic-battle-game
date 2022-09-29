from bender import bender

def avatar_game():
    elements = ['fire','water','earth','air']
    
    # Create 4 benders
    benders = [
        bender("Dragon",3,4,5,elements[0],True),
        bender("Moon",5,2,1,elements[1],True),
        bender("Badger Mole",4,5,3,elements[2],True),
        bender("Sky Bison",3,5,5,elements[3],True)
    ]
    dragon = benders[0]
    moon = benders[1]
    badger_mole = benders[2]
    bison = benders[3]

    # Begin Game
    print("-"*150)
    print("Welcome to the Avatar Battler!")
    print("-"*150)
    
    


if __name__ == "__main__":
    avatar_game()