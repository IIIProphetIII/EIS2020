from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2
import math
import numpy as np
from pykeyboard import PyKeyboard
import time
import os
mc=Minecraft.create()
k = PyKeyboard()
pos=mc.player.getTilePos()

def house(x,y,z):
    mc.setBlocks(x,y-1,z,x+9,y+5,z+9,5,block.COBBLESTONE.id)
    mc.setBlocks(x+1,y,z+1,x+9-1,y+4,z+9-1,0)  
    mc.setBlocks(x+3,y+1,z,x+4,y+2,z,block.GLASS.id)
    mc.setBlocks(x+6,y,z,x+6,y+1,z,64)              

while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
        f = open("move.txt")
        a =f.read()
        f.close()
        if a =='w':
            k.press_key("w")
            time.sleep(2)
            k.release_key("w")
            time.sleep(2)
        elif a =='a':
            k.press_key("a")
            time.sleep(2)
            k.release_key("a")
            time.sleep(2)
        elif a =='s':
            k.press_key("s")
            time.sleep(2)
            k.release_key("s")
            time.sleep(2)
        elif a =='d':
            k.press_key("d")
            time.sleep(2)
            k.release_key("d")
            time.sleep(2)
        elif a =='h':
            mc.player.setPos(110,2,-110)
            time.sleep(2)
        else:
            None
    if os.path.isfile("house.csv"):
        f = open("house.csv")
        pos = []
        for line in f:
            pos.append(line.split(","))
        f.close()
        house(int(pos[0][0]),int(pos[0][1]),int(pos[0][2]))
        break

