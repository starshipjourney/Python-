#!/usr/bin/env python3
"""
A Binary life simulation v1
"""
import numpy as np
import schedule
import time
import random
import os

def screen_clear(): #function to clear output screen
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#---The world---
world = np.zeros((15,15)).astype(int)
world = world.astype(str)

#---The Resource---
food_loc = []
def generate_food():
    index1 , index2 = random.randint(1,13),random.randint(1,13)
    if world[index1][index2] == '0':
        world[index1][index2] = f"F {random.randint(10,40)}" #F represents food with quantity of food it holds
        food_loc.append(world[index1][index2])
    # print(world,"\n")

schedule.every(random.randint(12,40)).seconds.do(generate_food) #food generation happens at random intervel between 8-16 sec

#---Our Binary life(Bot)---
class Binary():
    start_time = time.time()
    def __init__(self,index,name):
        self.index,self.name= index,name
        world[self.index[0]][self.index[1]] = self.name
        self.health = 100
        self.evolution = 1
    def purpose(self): #to find and eat food to survive
        if self.evolution == 1:
            hibernation_health = 90
        elif self.evolution == 2:
            hibernation_health = 120
        else:
            hibernation_health = 160
        if self.health < 0: #death
            print("YOUR BOT HAS DIED")
            print(f"BOT SURVIVED : {int(time.time()-Binary.start_time)} seconds","\n",f"BOT EVOLVED: lvl{self.evolution}")
            exit()
        elif self.health > hibernation_health: #at best health
            screen_clear()
            print("hibernating...",f"health is :{self.health}")
            self.health-=random.randint(2,5)
            print(world)
            pass
        else:
            screen_clear()
            binary_pos = np.argwhere(world==self.name)
            try: #if food is found
                food = [ np.argwhere(world == i) for i in food_loc]
                check_nearest = [np.linalg.norm(binary_pos - index) for index in food]
                index_of_distance = check_nearest.index(min(check_nearest))
                self.health-=int(min(check_nearest))
                for a,b in food[index_of_distance]: #for tuple unpacking
                    world[binary_pos] = '0'
                    world[a-1][b] = self.name
                    food_amount = world[a][b].split()
                    self.health+=int(food_amount[1])
                    print("i found food",f"health is :{self.health}")
                    print(world)
                    world[a][b]='0'
            except: #bot searches in random location
                health_hit = random.randint(0,10)
                if health_hit in range(5,8):
                    print("Your BOT : injured the leg")
                elif health_hit >= 8:
                    print("Your BOT : got stuck by ligtning") 
                self.health-=health_hit
                world[binary_pos] = '0'
                world[random.randint(0,14)][random.randint(0,14)]= self.name
                print("im searching for food",f"health is :{self.health}")
                print(world)
                pass
            finally: #clear memory of previous lists
                food_loc.clear()
                food.clear()
                check_nearest.clear()
    def evolve(self):
        if (self.evolution == 1) and (int(time.time()-Binary.start_time) > 120): #evolve to lvl 2
            print("Your Bot has EVOLVED !")
            self.health+=80
            self.evolution = 2
        elif (self.evolution == 2) and (int(time.time()-Binary.start_time) > 220): #evolve to lvl 3
            print("Your Bot has EVOLVED !")
            self.health+=80
            self.evolution = 3

bot_x1 = Binary([0,0],"X1")
schedule.every(3).seconds.do(bot_x1.purpose)
schedule.every(5).seconds.do(bot_x1.evolve)

while True: #keep our sheduler run forever
    schedule.run_pending()
    time.sleep(1)

