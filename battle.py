import itertools
import threading
import time
import sys

class Battle():
    
    def __init__(self, benders):
        self.benders = benders
   
    def battle_animation(self):
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rBattling! ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('')
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(2)
        done = True

    def battle(self):
        print("\n")
        while self.benders[0].health > 0 and self.benders[1].health > 0:
            self.benders[0].health -= self.benders[1].attack 
            self.benders[1].health -= self.benders[0].attack 
            print(self.benders[0].name+" health = "+str(self.benders[0].health))
            print(self.benders[1].name+" health = "+str(self.benders[1].health))
        
        if self.benders[0].health <= 0 and self.benders[1].health <= 0:
            print("Tie!")
            return

        winner = self.benders[0].name if self.benders[0].health > 0 else self.benders[1].name
        print(winner + " won!")
            
    def __str__(self):
        return "{} VS {}".format(self.benders[0], self.benders[1])

