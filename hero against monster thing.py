import json
import random

class hero:
    def __init__(self,Heroname: str,Herolevel: int,Herohealth: int,Heroexperience: int , Herodamage:int, Heroinventory):
        # attributes of our hero when we create it
        self.__heroname = Heroname
        self.herolevel = Herolevel
        self.herohealth = Herohealth
        self.heroexperience=  Heroexperience
        self.herodamage = Herodamage
        self.heroinventory = Heroinventory



Hero = {"name"} 


def create_hero():
    name = False
    while not name:
        global Heroname
        Heroname = input("please enter the name of your hero, appropriate length")
        Heroname_length = len(Heroname)
        if Heroname_length > 0 and Heroname_length < 20:
            Heroname = Heroname
            name = True 

















def Heroinventory():
    global inventory
    inventory = {"health" :{"item" : "regen"},
                        "damage":{ "item" : "attack"}}           

