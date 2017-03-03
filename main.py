#Untitled Project
import random

dirt = 0
grass = 0

while True:
    intake = input("> ")
    if intake == "":
        x = random.randint(1, 101)
        if x <= 50:
            dirt += 1
            print("Dirt:", dirt)
        else:
            grass += 1
            print("Grass:", grass)
