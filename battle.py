import itertools
import threading
import time
import sys
#from bender import Bender

class Battle():
    # def __init__(self,benders):
    #     self.benders = []
        
    # def add_benders(self,name,health,attack,speed,element):
    #     bender1 = new Bender(name,health,attack,speed,element)
    #     bender2 = new Bender(name,health,attack,speed,element)
    #     self.benders.extend((bender1,bender2))
    
    def battle_animation():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rBattling! ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            #sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(2)
        done = True
        
    # def determine_winner(self):
    #     print("This is the health of bender 1: "+self.bender1.health)