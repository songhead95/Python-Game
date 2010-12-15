import sys
import os
import random

################################################################################

MAPFILE="maps/world1.txt"
walkable = "."
mapping = {
    '.': ["you can't go there.", 0, 0, 0],
    '#': ["you walk into the wall... ouch! (-2 hp)",-2,0,0],
    '@': ["you bump into yourself... odd...", 0, 0, 0],
    'H': ["you fall into a trap door and die", -10000, 0, 0],
    '&': ["you eat the chicken and... oh my! it's poisoned! (-50 str), (-90 hp)", -90, -50, 1],
    '0': ["you try to touch and move the egg and it scalds your hand! (-8 hp)", -8, 0, 0],
    '~': ["you take a drink of the water... It's disguisting!! (-5 hp), (-5 str)", -5, -5, 1],
    'U':["you drink the strange elixer and feel nearly invincible!", 10000, 10000, 1, 'U'],
    '8': ["$enemy", 200, 15, "The barbarian strikes you and you stagger backwards", "You kill the barbarian"],
    '4': ["$enemy", 1000, 10, "The ferocious beast bites you", "you overpower the ghastly beast"],

}

class Player:
    X, Y, health, strength, name = 1,1,100,100, ""
    def namePlayer():
        sys.stdout.write("What is your name: ");
        name = raw_input()


user = Player()

###############################################################################
 
i=""
hit = False
copy2d = lambda matrix: [[i for i in l] for l in matrix]

def render ( array, x, y ):    
    sizex = len(array[0])
    sizey = len(array)-1
    print "+" + "=" * sizex + "+"
    data = copy2d(array)
    data[y][x]='@'
    for a in range(sizey):
        sys.stdout.write("|")
        for b in range(sizex):
            sys.stdout.write(data[a][b])
        print "|" 
    print "+" + "=" * sizex + "+"

   
def collide(point, my, mx):
    global hit
    hit = True
    if mapping[point][0]=="$enemy": 
        if(user.strength > random.randint(0, mapping[point][1])):
            print mapping[point][4]
            world[user.Y+my][user.X+mx]=0
        else:
            print mapping[point][3]
            user.health-= mapping[point][2]
    elif mapping[point][0]=="$stairs":
        floor+=mapping[point][1]
        print theMap[floor]
        user.Y = mapping[2]
        user.X = mapping[3]
    else:
        if mapping[point][3]==1:
            world[user.Y+my][user.X+mx]=0
        user.health+= mapping[point][1]  
        user.strength += mapping[point][2]
        print mapping[point][0]
 
def goUp():
    if(world[user.Y-1][user.X] != 0):
        collide(world[user.Y-1][user.X], -1, 0)
    else:
        user.Y-=1
 
def goDown():
    if(world[user.Y+1][user.X] != '.'):
        collide(world[user.Y+1][user.X], 1, 0)
    else:
        user.Y+=1
 
def goLeft():
    if(world[user.Y][user.X-1] != 0):
        collide(world[user.Y][user.X-1], 0, -1)
    else:
        user.X-=1
 
def goRight():
    if(world[user.Y][user.X+1] != 0):
        collide(world[user.Y][user.X+1], 0, 1)
    else:
        user.X+=1
 
def main():
    global world, hit
    world = open("maps/world1").read().split("\n")
    os.system("clear")
    print ""
    render(world, user.X, user.Y)
    print ' ' * ((len(world[1])/2)-4) + "WELCOME TO"
    print ' ' * ((len(world[1])/2)-1) + "BARF"
    i = " "
    sys.stdout.write("What is your name? > ")
    user.name = raw_input()
    while not i in ["quit", "q", "exit"]:
        hit = False
        sys.stdout.write(user.name + "> ")
        i = raw_input()
        os.system("clear")
        if(i in [ "go north", "north", "w" ]): goUp()
        if(i in [ "go south", "south", "s" ]): goDown()
        if(i in [ "go west", "west", "a" ]): goLeft()
        if(i in [ "go east", "east", "d" ]): goRight()
        if user.health> 0:
            if not hit: print ""
            render(world, user.X, user.Y)
            print "you have " + str(user.health) + " health, and " + str(user.strength) + " strength."
        else:
            print "You have died\n\n"
            raw_input()
            i = "q"




 

main()
