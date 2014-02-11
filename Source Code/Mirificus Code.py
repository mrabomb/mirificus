#!/usr/bin/python

# copyright Charles Chauncy 2013 


import time
import random
import os
import shutil

from os import system
system("title Mirificus")

#directories
east = open('directions/east.txt')
west = open('directions/west.txt')
south = open('directions/south.txt')
north = open('directions/north.txt')
up = open('directions/up.txt')
down = open('directions/down.txt')
caveentrence = open('directions/caveentrence.txt')
destroytree = open('directions/destroytree.txt')
lifttree = open('directions/lifttree.txt')
takerope = open('directions/takerope.txt')
checkinventory = open('directions/checkinventory.txt')
foundletter = open('directions/foundletter.txt')
foundsword = open('directions/foundsword.txt')
foundshovel = open('directions/foundshovel.txt')
moverock = open('directions/rock/moverock.txt')
bendrock = open('directions/rock/bending.txt')
destroyrock = open('directions/rock/destroy.txt')
rocknroll = open('directions/rock/rocknroll.txt')
tierope = open('directions/tierope.txt')
pulllever = open('directions/pulllever.txt')
takematch = open('directions/takematch.txt')
takekey = open('directions/takekey.txt')
eastereggnames = open('directions/eastereggnames.txt')
attack = open('directions/attack.txt')
push = open('directions/push.txt')
takebox = open('directions/takebox.txt')
unlockdoor = open('directions/unlockdoor.txt')
lighton = open('directions/lighton.txt')
lightoff = open('directions/lightoff.txt')
dig = open('directions/dig.txt')
flee = open('directions/flee.txt')
examineletter = open('directions/examine/letter.txt')
examinerope = open('directions/examine/rope.txt')
examinesword = open('directions/examine/sword.txt')
examineflashlight = open('directions/examine/flashlight.txt')
examineshovel = open('directions/examine/shovel.txt')
examinematches = open('directions/examine/matches.txt')
examinekey = open('directions/examine/key.txt')
excorn = open('directions/examine/excorn.txt')
examinefish = open('directions/examine/examinefish.txt')
examinerod = open('directions/examine/examinerod.txt')
examinecfish = open('directions/examine/examinecfish.txt')
examineletter = open('directions/examine/letter.txt')
examinerope = open('directions/examine/rope.txt')
examinesword = open('directions/examine/sword.txt')
examineflashlight = open('directions/examine/flashlight.txt')
examineshovel = open('directions/examine/shovel.txt')
examinematches = open('directions/examine/matches.txt')
examinekey = open('directions/examine/key.txt')
# userlist = open('directions/users/userlist.txt', 'a')
# save = open('directions/save.txt')
pay = open('directions/pay.txt')
swallow = open('directions/bridge/swallow.txt')
answer = open('directions/bridge/answer.txt')
maketorch = open('directions/maketorch.txt')
cook = open('directions/cook.txt')
fish = open('directions/fish.txt')
light = open('directions/light.txt')
takekindling = open('directions/kindling.txt')
wait = open('directions/wait.txt')
dive = open('directions/dive.txt')
speak = open('directions/speak.txt')
trade = open('directions/trade.txt')
buybatteries = open('directions/buybatteries.txt')
buysword = open('directions/buysword.txt')
sellsword = open('directions/sellsword.txt')
buyidol = open('directions/buyidol.txt')
sellidol = open('directions/sellidol.txt')
buyfiddle = open('directions/buyfiddle.txt')
sellfiddle = open('directions/sellfiddle.txt')
interact = open('directions/interact.txt')
changebattery = open('directions/changebattery.txt')



EastVars = east.read()
WestVars = west.read()
SouthVars = south.read()
NorthVars = north.read()
UpVars = up.read()
DownVars = down.read()
CaveEnterVars = caveentrence.read()
DestroyTreeVars = destroytree.read()
LiftTreeVars = lifttree.read()
TakeRopeVars = takerope.read()
CheckInventoryVars = checkinventory.read()
LetterVars = foundletter.read()
TakeSwordVars = foundsword.read()
TakeShovelVars = foundshovel.read()
MoveRock = moverock.read()
BendingRock = bendrock.read()
DestroyRock = destroyrock.read()
RockNRoll = rocknroll.read()
TieRopeVars = tierope.read()
PullLeverVars = pulllever.read()
TakeMatchVars = takematch.read()
TakeKeyVars = takekey.read()
EasterEggNames = eastereggnames.read()
AttackVars = attack.read()
PushVars = push.read()
TakeBoxVars = takebox.read()
UnlockDoor = unlockdoor.read()
LightOnVars = lighton.read()
LightOffVars = lightoff.read()
DigVars = dig.read()
FleeVars = flee.read()
ExamineLetterVars = examineletter.read()
ExamineRopeVars = examinerope.read()
ExamineSwordVars = examinesword.read()
ExamineFlashlightVars = examineflashlight.read()
ExamineShovelVars = examineshovel.read()
ExamineMatchesVars = examinematches.read()
ExamineKeyVars = examinekey.read()
# Username = userlist.read()
# SaveVars = save.read()
PayVars = pay.read()
SwallowVars = swallow.read() 
AnswerVars = answer.read()
FishVars = fish.read()
LightVars = light.read()
TakeKindlingVars = takekindling.read()
WaitVars = wait.read()
MakeTorchVars = maketorch.read()
DiveVars = dive.read()
SpeakVars = speak.read()
TradeVars = trade.read()
BuyBatteriesVars = buybatteries.read()
BuySwordVars = buysword.read()
SellSwordVars = sellsword.read()
BuyIdolVars = buyidol.read()
SellIdolVars = sellidol.read()
BuyFiddleVars = buyfiddle.read()
SellFiddleVars = sellfiddle.read()
InteractVars = interact.read()
ChangeBatteryVars = changebattery.read()



#list for places items can be
inventory = []
dwarfstore = ['batteries']

startareafloor = []
pineforestfloor = []
oakforestfloor = [] 
meadowfloor = []
lakefloor = ['rope']
cavefloor = []
bramblesfloor = ['letter']
swordinstonefloor = ['sword']
smalltunnelfloor = []
skylightfloor = []
hillsfloor = []
rockhillsfloor = ['flashlight']
stonearchwayfloor = ['shovel']
stairsfloor = []
crumblingwallfloor = ['matches']
keyroomfloor = ['key']
darkroomfloor = ['box']
darkgatefloor = []
goalfloor = ['box']
canyonlakefloor = ['gold']


fallentree = ['tree']
rockobstruction = ['rock']

gratelist = []
leverup = ['lever']
leverdown = []
flashon = []
flashoff = ['state']
fightlist = ['demon']

bridgeguard = []
paydoorguard = []

day = ['sun']

manlocation = ['rock']



#variables
timeday = 1
torchtime = 1
corncob = 1
gold = 0
kindling = 0
checkpoint = 0
formalities = 0
flashlife = 200





#some subroutines

def intro():
    print("\n\nYou awaken in a clearing"); time.sleep(2)
    print("You have no memories of how you got there"); time.sleep(2)
    print("Come to think of it, you can't even remember who you are"); time.sleep(3)
    print("\nAlthough this situation is distressing, you seem to be");time.sleep(2)
    print("an individual who keeps their priorities straight and has"); time.sleep(2)
    print("an inpeccable sense of direction, you know that"); time.sleep(2)
    print("the first step is to decide what to call yourself");time.sleep(2)
    print("at least until you regain your memories.\n");time.sleep(2)
    print("So what will it be?\n")

    global CharName
    CharName = input("(Give yourself a name)\n\n>>"); time.sleep(.5)
    CharName = CharName.upper()
    
    if CharName in EasterEggNames:
        if CharName == 'ADMIN':
            print("\n\nYou feel the godly powers flow through you"); time.sleep(1)
            print("You weild the mighty banhammer!"); time.sleep(1.5)
            print("(Seriously, nice choice of names)"); time.sleep(2)
        elif CharName == 'KRONK':
            print("\n\nYou're rough, you're tough and you're voiced by Patrick Warburton");time.sleep(1.5)
            print("Time to get your groove on,", CharName);time.sleep(2)
        elif CharName == 'LINK':
            print("\nHmmm... It seems that somewhere the hero of time has awoken...");time.sleep(2)
            print("Anyway, you decide to don the green clothes you found", CharName);time.sleep(2)
            print("and get to business");time.sleep(1)
    else:
        print("\n\nHmmm...", CharName," is as good a name as any."); time.sleep(1.5)
        print("From now on, your name will be", CharName)
        time.sleep(2)
    return


def lightsource():
    global lightlevel
    if 'flashlight' in inventory:
        if 'state' in flashon:
            lightlevel = 1
        else:
            lightlevel = 0
    elif 'torch' in inventory:
        lightlevel = 1
    else:
        lightlevel = 0
    return



def death():
    print("The grue drags you to a room with a strange altar in the center"); time.sleep(2)
    print("Your uncouncious body is placed on the altar"); time.sleep(1)
    print("Grues begin to enter the room from all directions, as if from \nthe darkness itself");time.sleep(2)
    print("They feast upon you");time.sleep(2)
    print("You have died,", CharName);time.sleep(1)
    spawn = input("Would you like to respawn?\n'yes' or 'no'\n\n>>")
    if spawn == 'yes':
        cls()
        print("Respawn in 9");time.sleep(1); cls()
        print("Respawn in 8");time.sleep(1); cls()
        print("Respawn in 7");time.sleep(1); cls()
        print("Respawn in... lets cut to the chase");time.sleep(2); cls()
        print("Respawn in 1");time.sleep(1); cls()     

    else:
        print("Thats game over")
        print("But who wouldn't want to respawn?");time.sleep(3); cls()
        print("Respawn in 9");time.sleep(1); cls()
        print("Respawn in 8");time.sleep(1); cls()
        print("Respawn in 7");time.sleep(1); cls()
        print("Respawn in... lets cut to the chase");time.sleep(2); cls()
        print("Respawn in 1");time.sleep(1); cls()
    if checkpoint == 1:
        cloverfield()
    else:
        startarea()
    return


def probability():
    global lightlevel
    if (lightlevel == 0):
        grueprob = random.randint(1, 10)
        if grueprob == 10:
            print("You have encountered the most fearsome of beasts, the grue.");time.sleep(2)
            print("It looks like this is the end.");time.sleep(1)
            print("The grue beats you uncouncious and begins to drag you");time.sleep(2)
            death()
        else:
            print("It is dark, you should probably find a light source soon")
    else:
        eyecorner = random.randint(1, 100)
        if eyecorner == 10:
            print("You see something move out of the corner of your eye."); time.sleep(1.5)
            print("Something is watching you from the dark"); time.sleep(1)
            print("It would be best to leave as quickly as possible");time.sleep(1.5)
        else:
            pass
    return


def cls():         #this clears the screen (just encase that wasn't obvious)
    time.sleep(1)
    os.system(['clear','cls'][os.name == 'nt'])
    return


def examine():
    if movement in ExamineRopeVars:
        if 'rope' in inventory:
            print("\nThe rope appears to be both very long and very strong\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineLetterVars:
        if 'letter' in inventory:
            print("\nYou read the letter:")
            print("'Dear player, I hope you like text based games");time.sleep(.6)
            print("If you don't, then you're about to learn to!");time.sleep(.6)
            print("Here we have untold numbers of hours of work");time.sleep(.6)
            print("But it can certainly be improved");time.sleep(.6)
            print("If you want, feel free to improve it, as it is");time.sleep(.6)
            print("Open source. Email me a copy of your changes");time.sleep(.6)
            print("If I like what you've done, I will upload it in the official version");time.sleep(1)
            print("My email is Makeanewname@gmail.com'");time.sleep(.6)
            print("\n\nIt seems like that letter was meant for someone else...")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineSwordVars:
        if 'sword' in inventory:
            print("\nThe sword is beutifully crafted and very sharp\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineFlashlightVars:
        if 'flashlight' in inventory:
            if 'state' in flashon:
                print("\nThe flashlight is on\n")
            else:
                print("\nThe flashlight is off\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineShovelVars:
        if 'shovel' in inventory:
            print("\nYou could dig with this\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineMatchesVars:
        if 'matches' in inventory:
            print("\nThere appears to be an almost endless number of strike anywhere matches\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in ExamineKeyVars:
        if 'key' in invetory:
            print("\nDoes this open a door?\n")
        else:
            print("\nI don't think that will work\n")
    else:
        print("\nI don't think that will work\n")
    return


def clock():                                                  # this makes time pass
    global timeday
    global sunlight
    global flashlife
    timeday = timeday + 1
    change = timeday%12

    if 'flashlight' in inventory:
        if 'state' in flashon:
            flashlife = flashlife - 1
            lifechange = flashlife%50

            if lifechange == 3:
                print("\nYour flashlight is at 75% capacity")
            elif lifechange == 2:
                print("\nYour flashlight is at 50% capacity")
            elif lifechange == 1:
                print("\nYour flashlight is at 25% capacity")
            elif lifechange == 0:
                print("\nThe light from the flashlight flickers and dies")
        else:
            pass
    else:
        pass


    if 'torch' in inventory:
        torchtime = torchtime + 1
        torchchange = torchtime%15

        if torchchange == 0:
            print("\nThe torch has burned out\n")
            inventory.remove('torch')
        elif torchchange == 5:
            print("\nThe light from the torch is beginning to waver\n")
        elif torchchange == 10:
            print("\nThe light from the torch is beginning to dim\n")
            
    else:
        pass
        

    if change == 0:
        if 'sun' in day:
            print("\nThe sun has set\n")
            day.remove('sun')
        else:
            print("\nThe sun has risen\n")
            day.append('sun')
    elif change == 3:
        if 'sun' in day:
            print("\nThe sun is a quarter of the way through the sky\n")
        else:
            print("\nThe moon is a quarter of the way through the sky\n")
    elif change == 6:
        if 'sun' in day:
            print("\nThe sun is halfway through the sky\n")
        else:
            print("\nThe moon is halfway through the sky\n")
    elif change == 9:
        if 'sun' in day:
            print("\nThe sun will set soon\n")
        else:
            print("\nThe sun will rise soon\n")
    else:
        pass
    return
    
    

def sunroutine():                                                # this adds a lightlevel to day/night
    global lightlevel
    if 'sun' in day:
        lightlevel = 1
    else:
        lightlevel = 0
    return



def userdata():
    global User
    User = input("USERNAME: ")
    User = User.upper()
    cls()
    print("USERNAME:",User)
    
    if User in Username:
        pass
    else:
        pass
    return



def savegame():
    global User
    if movement in SaveVars:   
        userlistwrite.write(User)
        shutil.copyfile("Play.py", "directions/saves/"+User+'.py')
        print("\nGAME SAVED\n")
    else:
        pass
    return



def routines():                                                 #routines that are used everywhere
    global gold
    if movement in LightVars:
        lighttoggle()
    elif movement in CheckInventoryVars:
        inventorycheck()
    elif movement in WaitVars:
        wait()
    elif movement in ChangeBatteryVars:
        changebatteries()
    elif movement in DigVars:
        digfortreasure()
    else:
        examine()
    return

def digfortreasure():
    global gold
    if 'shovel' in inventory:
        print("\nYou take a moment to dig"); time.sleep(1)
        if checkpoint > 0:
            clock()
            if 'lucky clover' in inventory:
                foundobject = random.randint(1, 15)
                if foundobject == 7:
                    foundgold = random.randint(1, 20)
                    print("\nYou found", foundgold, "gold coins")
                    gold = gold + foundgold
                else:
                    print("\nYou didn't find anything of value")
            else:
                foundobject = random.randint(1, 30)
                if foundobject == 7:
                    foundgold = random.randint(1, 20)
                    print("\nYou found", foundgold, "gold coins")
                    gold = gold + foundgold
        else:
            print("\nYou didn't find anything of value")
    else:
        print("\nI don't think that will work")
    return

def changebatteries():
    global flashlife
    if 'batteries' in inventory:
        print("\nYou replace the batteries in the flashlight, discarding the used batteries")
        inventory.remove('batteries')
        flashlife = 200
    else:
        print("\nI don't think that will work")
    return

def lighttoggle():
    if movement in LightOnVars:
        if 'flashlight' in inventory:
            if 'state' in flashoff:
                print("You turn the flashlight on\n")
                flashoff.remove('state')
                flashon.append('state')
            else:
                print("\nI don't think that will work\n")
        else:
            print("\nI don't think that will work\n")
    elif movement in LightOffVars:
        if 'flashlight' in inventory:
            if 'state' in flashon:
                print("You turn the flashlight off\n")
                flashon.remove('state')
                flashoff.append('state')
            else:
                print("\nI don't think that will work\n")
        else:
            print("\nI don't think that will work\n")
    return

def inventorycheck():
    global gold
    global kindling
    print("\nYou look into your bag and see:")

    if 'golden idol' in inventory:
        print("A Golden Idol")
    else:
        pass
    if 'matches' in inventory:
        print("A Box of Matches")
    else:
        pass
    if 'cooked fish' in inventory:
        print("A Cooked Fish")
    else:
        pass
    if 'corn cob' in inventory:
        print("An Ear of Corn")
    else:
        pass
    if 'cooked corn' in inventory:
        print("Some Cooked Corn")
    else:
        pass
    if 'golden fiddle' in inventory:
        print("A Fiddle Made of Solid Gold")
    else:
        pass
    if 'fishing rod' in inventory:
        print("A Fishing Rod")
    else:
        pass
    if 'flashlight' in inventory:
        print("A Flashlight")
    else:
        pass
    if 'lucky clover' in inventory:
        print("A Four-Leafed Clover")
    else:
        pass
    if 'vial' in inventory:
        print("A Glass Vial\n")
    else:
        pass
    if 'key' in inventory:
        print("A Golden Key")
    else:
        pass
    if 'letter' in inventory:
        print("A Letter")
    else:
        pass
    if 'raw fish' in inventory:
        print("A Raw Fish")
    else:
        pass
    if 'rope' in inventory:
        print("A Rope")
    else:
        pass
    if 'shovel' in inventory:
        print("A Shovel")
    else:
        pass
    if 'sword' in inventory:
        print("A Beautiful Elven Sword")
    else:
        pass
    if 'batteries' in inventory:
        print("Some Flashlight Batteries")
    else:
        pass
    if gold > 0:
        print("You have", gold, "gold coins")
    else:
        pass
    if kindling > 0:
        print("You have enough kindling to make", kindling, "fires")

    if gold == 0 and kindling == 0 and inventory == []:
        print("Nothing!")
    else:
        pass
    return


def kindlingchance():
    global kindlingprob
    if kindling < 10:
        kindlingprob = random.randint(1, 4)
    else:
        kindlingprob = 1
    return


def wait():
    global checkpoint
    
    if checkpoint > 0:
        print("\nYou take a break and allow a few hours to pass")
        clock()
    else:
        pass
    return


def maketorch():
    global kindling
    global movement

    if movement in MakeTorchVars:
        if 'torch' in inventory:
            print("\nYou don't need a second torch")
        else:
            if 'matches'in inventory:
                if kindling > 1:
                    inventory.append('torch')
                    kindling = kindling - 1
                    print("\nYou use the matches to light some kindling and fashion a torch"); time.sleep(.5)
                    print("The torch looks like it will burn for about 15 hours")
                else:
                    pass
            else:
                pass
    else:
        pass
    return


def checkpointlight():

    if checkpoint > 0:
        lightsource()
        sunroutine()
        probability()
        clock()
    else:
        pass
    return




#subroutines for the rooms
    

def startarea():
    global movement
    global gold
    global checkpoint
        
    print("\nThere appear to be paths to the north, east, south, and west.")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("\nThe trail leads deep into an old oak forest")
        checkpointlight()
        oakforest()
    elif movement in NorthVars:
        print("\nYou begin walking north along a narrow path.");time.sleep(1.5)
        print("You come across a bridge to the north, streched out over a canyon\n")
        checkpointlight()
        bridge()
    elif movement in WestVars:
        print("\nThe trail leads into a thick pine forest")
        checkpointlight()
        pineforest()
    elif movement in SouthVars:
        print("\nThe trail leads to a grassy meadow")
        checkpointlight()
        meadow()
    else:
        routines()
        startarea()
    return


                
def pineforest():
    global movement
    global gold
    global kindling
    kindlingchance()
    global kindlingprob

    print("\nThere is a trail to the east and one to the north.")
    if 'tree' in fallentree:
        print("The path to the north is blocked by a fallen redwood tree.\n")
    else:
        pass

    if 'kindling' not in pineforestfloor:
        if kindlingprob == 2:
            oakforestfloor.append('kindling')
        else:
            pass
    else:                                                         #it needs both if statements because it needs to do one then the other
        pass
    if 'kindling' in pineforestfloor:
        print("\nSome sticks that may be good for kindling are just off the trail")
    else:
        pass


    movement = input("\n>>")
    movement = movement.lower()    
    cls()

    if movement in EastVars:
        print("\nThe trail leads to the area you awoke")
        checkpointlight()
        startarea()
    elif movement in DestroyTreeVars:
        if 'tree' in fallentree:
            if 'matches' in inventory:
                fallentree.remove('tree')
                print("You have successfully removed the tree, the north pathway has been cleared")
                pineforest()
            else:
                print("\nYou may need something else in order to do that")
                pineforest()
        else:
            print("You already did that")
            pineforest()
    elif movement in LiftTreeVars:
        if 'tree' in fallentree:
            print("\nYou arn't nearly strong enough to lift a tree of this size")
            pineforest()
        else:
            print("The tree has already been removed")
            pineforest()
    elif movement in NorthVars:
        if 'tree' in fallentree:
            print("\nThere is a tree blocking this pathway, maybe something can be done about that...")
            pineforest()
        else:
            print("\nA building is visible up ahead"); time.sleep(1)
            checkpointlight()
            goal()
    elif movement in TakeKindlingVars:
        if 'kindling' in oakforestfloor:
            kindling = kindling + 1
            oakforestfloor.remove('kindling')
            print("\nYou gather some kindling off the forest floor")
            pineforest()
        else:
            print("\nI don't think that will work")
            pineforest()
    else:
        routines()
        pineforest()
    return


    
def oakforest():
    global movement
    global gold
    global kindling
    kindlingchance()
    global kindlingprob



    print("\n\nThere is a pathway to the east, west, and a cave to the north")

    if 'kindling' not in oakforestfloor:
        if kindlingprob == 2:
            oakforestfloor.append('kindling')
        else:
            pass
    else:                                                         #it needs both if statements because it needs to do one then the other
        pass
    if 'kindling' in oakforestfloor:
        print("\nSome sticks that may be good for kindling are just off the trail")
    else:
        pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("The path quickly becomes overgrown with brambles and thorns")
        checkpointlight()
        brambles()
    elif movement in CaveEnterVars:
        print("\nThere is a sign on the cave, would you like to read it?")
        readsign = input("'yes' or 'no'\n>>")

        if readsign == 'yes':
            print("\nBEWARE! Grues hide in the dark!\nIt isn't safe to travel without a light source!\n")

            lightsource()

            if lightlevel == 1:
                print("\nYou walk through the cave entrance")
                cave()
            else:
                print("\nYou should really have a light with you before you do this")
                entercave = input("Are you sure you want to go in without a light? \n('yes' or 'no')\n>>")

                if entercave == 'yes':
                    print("\nYou walk through the cave entrance")
                    cave()
                else:
                    print("Maybe find a light before you come back")
                    oakforest()
        else:
            lightsource()

            if lightlevel == 1:
                print("\nYou walk through the cave entrance")
                cave()
            elif lightlevel == 0:
                print("\nYou should really have a light with you before you do this")
                entercave = input("\nAre you sure you want to go in without a light? \n('yes' or 'no')\n\n>>")

                if entercave == 'yes':
                    print("\nYou walk through the cave entrance")
                    cave()
                else:
                    print("Maybe find a light before you come back")
                    oakforest()
    elif movement in WestVars:
        print("\nThe trail leads to the area you awoke")
        checkpointlight()
        startarea()
    elif movement in TakeKindlingVars:
        if 'kindling' in oakforestfloor:
            kindling = kindling + 1
            oakforestfloor.remove('kindling')
            print("\nYou gather some kindling off the forest floor")
            oakforest()
        else:
            print("\nI don't think that will work")
            oakforest()
    else:
        routines()
        oakforest()     
    return




def meadow():
    global movement
    global gold
    print("\n\nPathways are visible to the north, east, and west")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("\nThe path winds through some rolling hills\n")
        checkpointlight()
        hills()
    elif movement in WestVars:
        print("\nThe trail leads to a pristine, blue lake\n")
        checkpointlight()
        lake()
    elif movement in NorthVars:
        print("\nThe trail leads to the area you awoke\n")
        checkpointlight()
        startarea()
    else:
        routines()
        meadow()
    return



def lake():
    global gold
    global movement
    if 'rope' in lakefloor:
        print("\nThere is a ropeswing hanging from a tree over the lake.\nThe knot looks easy to untie\n")
    else:
        print("\nThere is a tree over the lake that looks\nlike there used to have a ropeswing tied to it\n")

    print("The only pathway away from the lake is to the east\n")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    
    if movement in EastVars:
        print("\nThe trail leads to a grassy meadow\n")
        checkpointlight()
        meadow()
    elif movement in TakeRopeVars:
        if 'rope' in lakefloor:
            lakefloor.remove('rope')
            inventory.append('rope')
            print("\nYou untie the rope and put it into your inventory")
            lake()
        else:
            print("You've already taken that")
            lake()
    elif movement in FishVars:
        if 'fishing rod' in inventory:
            if 'raw fish' not in inventory:
                print("\nYou cast out your line and wait for a fish to bite");time.sleep(3)
                if 'lucky clover' in inventory:
                    catchfish = random.randint(1, 5)
                    lake()
                else:
                    catchfish = random.randint(1, 20)
                    lake()
                if catchfish == 5:
                    print("\nYou caught a fish!");time.sleep(1.5)
                    print("With the proper preperation, this could be quite tasty");time.sleep(1)
                    print("You place the fish in your inventory\n");time.sleep(2)
                    inventory.append('raw fish')
                    lake()
                else:
                    print("\nYou did not catch a fish\n");time.sleep(2)
                    lake()
            else:
                print("\nYou already have a fish with you");time.sleep(2)
                lake()
        else:
            print("\nYou need a fishing rod to do that");time.sleep(2)
            lake()
    elif movement == 'swing' or 'swing on rope' or 'swing on rope swing':
        if 'rope' in lakefloor:
            print("\nYou swing on the rope into the lake"); time.sleep(.5)
            print("After a refreshing swim you exit the lake")
            lake()
        else:
            print("You took down the ropeswing, you can't swing now")
            lake()
    elif movement == 'swim' or 'go swimming' or 'dive':
        print("\nYou dive into the water");time.sleep(.5)
        print("After a refreshing swim you exit the lake")
        lake()
    else:
        routines()
        lake()
    return    

              

def cave():
    global movement
    global gold
    lightsource()    
    probability()

    print("\nThe main cave leads towards the north, however there appears to be a small \nopening to the west")
    print("The cave exit is to the south")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in NorthVars:
        print("\nYou walk to the back of the cave\n")
        swordinstone()
    elif movement in WestVars:
        print("\nYou wiggle through the small opening and into a very small tunnel\n")
        smalltunnel()
    elif movement in SouthVars:
        print("\nThe trail leads deep into an old oak forest")
        oakforest()
    else:
        routines()
        cave()
    return




def brambles():
    global movement
    global gold
    print("There is only a pathway to the west")

    if 'letter' in bramblesfloor:
        print("There is a piece of paper stuck on one of the thorns")
    else:
        pass
        
    movement = input("\n>>")
    movement = movement.lower() 
    cls() 
    
    if movement in WestVars:
        print("\nThe trail leads deep into an old oak forest")
        checkpointlight()
        oakforest()
    elif movement in LetterVars:
        if 'letter' in bramblesfloor:  
            bramblesfloor.remove('letter')
            inventory.append('letter')
            print("You take the letter and place it into your inventory")
            brambles()
        else:
            print("You've already taken that")
            brambles()
    else:
        routines()
        brambles()
    return



def swordinstone():
    global movement
    global gold
    lightsource()
    probability()

    print("The only exit is to the south")

    if 'sword' in swordinstonefloor:
        print("There is a a beautifull crafted sword stuck into the rock")
        print("on the far wall")
    else:
        pass
    
    movement = input("\n>>")
    movement = movement.lower()
    cls()
    
    if movement in SouthVars:
        print("You walk back through the cave towards the entrance")
        cave()
    elif movement in TakeSwordVars: 
        if 'sword' in swordinstonefloor:
            print("You take the sword and place it into your inventory")
            swordinstonefloor.remove('sword')
            inventory.append('sword')
            swordinstone()
        else:
            print("You've already taken that")
            swordinstone()
    else:
        routines()        
        swordinstone()
    
    return



def smalltunnel():
    global movement
    global gold
    lightsource()
    probability()
    
    print("There is a light coming from the north and the cave exit\nis to the east")
    
    movement = input("\n>>")
    movement = movement.lower()
    cls()
    
    if movement in NorthVars:
        print("You crawl out of the cramped tunnel and into a room with an\nopening at the top")
        skylight()
    elif movement in EastVars:
        print("You leave the small tunnel and walk towards the cave entrance")
        cave()
    else:
        routines()
        smalltunnel()
    return



def skylight():
    global movement
    global gold
    print("Although there is some natural light here, you instictively know\nthat it won't be enough to scare anything away")
    lightsource()
    probability()

    print("The cave has two passages, one leading to the west and one to the south.")

    movement = input("\n>>")
    movement = movement.lower()
    cls()
    
    if movement in WestVars:
        print("\nYou approach a passageway with a large staircase in the center")
        stairs()
    elif movement in SouthVars:
        print("\nYou wiggle through the small opening and into a very small tunnel\n")
        smalltunnel()
    else:
        routines()
        skylight()
    return


def hills():
    global movement
    global gold
    print("There are pathways to the east, south, and west")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("You approach a strange circular set of stone archways")
        checkpointlight()
        stonearchway()
    elif movement in SouthVars:
        print("As you walk you begin to notice large rocks dotting the hillside")
        checkpointlight()
        rockyhills()
    elif movement in WestVars:
        print("\nThe trail leads to a grassy meadow")
        checkpointlight()
        meadow()
    else:
        routines()
        hills()
    return


def rockyhills():
    global movement
    global gold
    global CharName
    
    print("The path dead ends. The only path heads to the north.")
          
    if 'rock' in rockobstruction:
        print("\nThere is a strange rock at the end of the path")
        print("It looks moveable")
    else:
        if 'flashlight' in rockhillsfloor:
            print("The ground under where the rock was seems freshly turned")
        else:
            pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()
        
    if movement in MoveRock:
        if 'rock' in rockobstruction:
            print("You move the rock from the path"); time.sleep(.5)
            rockobstruction.remove('rock')
            rockyhills()
        else:
            print("The rock has already been moved")
            rockyhills()
    elif movement in BendingRock:
        if 'rock' in rockobstruction:
            print("You use your mighty Avatar powers to remove the rock from the path")
            rockobstruction.remove('rock')
            rockyhills()
        else:
            print("The rock has already been moved")
            rockyhills()
    elif movement in DestroyRock:
        if 'rock' in rockobstruction:
            if CharName == 'ADMIN':
                print("You weild your mighty banhammer against the rock"); time.sleep(1)
                print("The rock is no more")
                rockobstruction.remove('rock')
                rockyhills()
            else:
                print("You continually hit the rock"); time.sleep(1)
                print("Eventually the rock breaks in half"); time.sleep(1)
                print("The halves crumble away to dust")
                rockobstruction.remove('rock')
                rockyhills()
        else:
            print("The rock has already been moved")
            rockyhills()
    elif movement in RockNRoll:
        if 'rock' in rockobstruction:
            print("You feel music flow through your bones"); time.sleep(1)
            print("The power of Rock compells you!"); time.sleep(1)
            print("Although you now could rival Eddie Van Halen,"); time.sleep(.5)
            print("the rock has not been moved")
            rockyhills()
        else:
            print("A guitar appears from nowhere and you proceed"); time.sleep(1)
            print("to rock out!")
            rockyhills()
    elif movement in NorthVars:
        print("\nThe path winds through some rolling hills\n")
        checkpointlight()
        hills()
    elif movement in DigVars:
        if 'flashlight' in rockhillsfloor:
            if 'shovel' in inventory:
                print("\nYou dig into the freshly turned soil");time.sleep(1)
                print("You found a flashlight!");time.sleep(1)
                print("You place the flashlight in your inventory")
                rockhillsfloor.remove('flashlight')
                inventory.append('flashlight')
                rockyhills()
            else:
                print("\nI don't think that will work\n")
                rockyhills()
        else:
            print("\nI don't think that will work\n")
            rockyhills()
    else:
        routines()
        rockyhills()
    return


def stonearchway():
    global movement
    global gold
    print("\nThe only path is to the west")
          
    if 'shovel' in stonearchwayfloor:
        print("\nA shovel is leaning against one of the strange arch-like rock formations\n")
    else:
        pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in WestVars:
        print("\nThe path winds through some rolling hills\n")
        checkpointlight()
        hills()
    elif movement in TakeShovelVars:
        if 'shovel' in stonearchwayfloor:
            print("\nYou take the shovel and place it in your inventory\n")
            stonearchwayfloor.remove('shovel')
            inventory.append('shovel')
            stonearchway()
        else:
            print("You've already taken that")
            stonearchway()
    else:
        routines()
        stonearchway()
    return


def stairs():
    global movement
    global gold
    print("\nThere are openings to the north and east and a stairwell leading downward\n")
    lightsource()
    probability()

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in NorthVars:
        print("\nThere is moss growing all along the floor and walls of the cave")
        mossypath()
    elif movement in EastVars:
        print("You walk back into the room with an opening at the top")
        skylight()
    elif movement in DownVars:
        print("\nYou descend into a large cavern with strange pillars evenly \nspaced around the room\n")
        pillarcavern()  
    else:
        routines()
        stairs()
    return


def mossypath():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThere is are openings to the east and south.");time.sleep(1)
    print("\nThe path to the east gives off a strange malice.")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        enter = input("Are you sure you really want to do this?\n>>")
        if enter == 'yes':
            print("You walk down the eastern tunnel")
            darkroom()
        else:
            print("Maybe that is the right decision"); time.sleep(1)
            mossypath()
    elif movement in SouthVars:
        print("\nYou approach a passageway with a large staircase in the center")
        stairs()
    else:
        routines()
        mossypath()    
    return


def pillarcavern():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThere are openings to the north and south and a stairway upward\n")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in UpVars:
        print("\nYou approach a passageway with a large staircase in the center")
        stairs()
    elif movement in NorthVars:
        print("\nYou walk into a strange square cavern")
        hiddendoor()
    elif movement in SouthVars:
        print("\nYou squeeze into a narrow passageway")
        narrowhall()
    else:
        routines()
        pillarcavern()    
    return


def narrowhall():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThe narrow passage has exits to the north and south\n")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in NorthVars:
        print("\nYou squeeze into a large cavern with strange pillars evenly\nspaced around the room\n")
        pillarcavern()
    elif movement in SouthVars:
        print("\nYou walk into a room with a huge dark gateway along one wall")
        darkgate()
    else:
        routines()
        narrowhall()        
    return


def darkgate():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThere is a large black gateway along the western wall");time.sleep(1)
    print("You feel a dark force eminating from it");time.sleep(1)
    print("\nThere are also openings to the north and south")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SouthVars:
        print("\nThe cavern leads to a steep precipe\n")
        precipe()
    elif movement in NorthVars:
        print("\nYou squeeze into a narrow passageway\n")
        narrowhall()
    elif movement in WestVars:
        print("\nAlthough their seems to be a path beyond the gateway,");time.sleep(1)
        print("Some sort of barrier seems to be blocking your way\n")
        darkgate()
    else:
        routines()
        darkgate()  
    return


def precipe():
    global movement
    global gold
    lightsource()
    probability()

    print("There are openings to paths to the north and east\nand a huge precipe to the south");time.sleep(1)
    if 'rope' in gratelist:
        print("\nA rope is dangling from the grate down into the void\n")
    else:
        print("\nThere is a metal grate on the wall near the precipe\n")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in NorthVars:
        print("\nYou walk into a room with a huge dark gateway along one wall\n")
        darkgate()
    elif movement in EastVars:
        print("\nThe path leads to a large cavern with a small crumbling wall in the center\n")
        crumblingwall()
    elif movement in TieRopeVars:
        if 'rope' in inventory:
            print("\nYou tie the rope to the grating and dangle the other end over the precipe\n")
            inventory.remove('rope')
            gratelist.append('rope')
            precipe()
        else:
            print("\nYou climb down the rope into an open room with a lever on the far wall")
            leverroom()
    elif movement in DownVars:
        if 'rope' in gratelist:
            print("\nYou climb down the rope into an open room with a lever on the far wall")
            leverroom()
        else:
            print("\nThe precipe is too steep to climb down")
            precipe()
    else:
        routines()
        precipe()
    return


def leverroom():
    global movement
    global gold
    lightsource()
    probability()

    if 'lever' in leverup:
        print("\nThe lever is up\n")
    elif 'lever' in leverdown:
        print("\nThe lever is down\n")
    else:
        pass

    print("The only exit is back up the rope")

    movement = input("\n>>")
    movement = movement.lower()
    cls()
    
    if movement in UpVars:
        print("\nThe cavern leads to a steep precipe\n")
        precipe()
    elif movement in PullLeverVars:
        if CharName == 'KRONK':
            if 'lever' in leverup:
                print("\nYzma screams 'Pull the lever Kronk!'")
                print("You pull the lever down");time.sleep(1)
                print("Yzma falls into a crocodile pit")
                print("In the distance you hear a loud grinding sound")
                print("Yzma climbs out of the crocodile pit and is not very happy\n")
                leverup.remove('lever')
                leverdown.append('lever')
                leverroom()
            elif 'lever' in leverdown:
                print("\nYzma screams 'Pull the lever Kronk!'")
                print("You push the lever up");time.sleep(1)
                print("Yzma falls into a crocodile pit")
                print("In the distance you hear a loud grinding sound")
                print("Yzma climbs out of the crocodile pit and is not very happy\n")
                leverdown.remove('lever')
                leverup.append('lever')
                leverroom()
        else:
            if 'lever' in leverup:
                print("\nYou pull the lever down");time.sleep(1)
                print("In the distance you hear a loud grinding sound\n")
                leverup.remove('lever')
                leverdown.append('lever')
                leverroom()
            elif 'lever' in leverdown:
                print("\nYou push the lever up");time.sleep(1)
                print("In the distance you hear a loud grinding sound\n")
                leverdown.remove('lever')
                leverup.append('lever')
                leverroom()
    else:
        routines()
        leverroom()
    return


def crumblingwall():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThere is an opening to the west\n")
    if 'matches' in crumblingwallfloor:
       print("It looks like there is a matchbox on the wall in the middle of the cavern\n")
    else:
       pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in WestVars:
        print("\nThe cavern leads to a steep precipe\n")
        precipe()
    elif movement in TakeMatchVars:
        if 'matches' in crumblingwallfloor:
            print("\nYou take the matchbox and place it in your inventory\n")
            crumblingwallfloor.remove('matches')
            inventory.append('matches')
            crumblingwall()
        else:
            print("You've already done that")
            crumblingwall()
    else:
        routines()
        crumblingwall()
    return


def hiddendoor():
    global movement
    global gold
    lightsource()
    probability()

    print("\nThe room is completely empty\nThere is a pathway to the south\n")
    if 'lever' in leverdown:
        print("\nA hidden door has opened in the western wall\n")
    else:
        pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SouthVars:
        print("\nYou enter a large cavern with strange pillars evenly \nspaced around the room\n")
        pillarcavern()
    elif movement in WestVars:
        if 'lever' in leverdown:
            print("\nYou walk into what appears to be yet another empty room")
            keyroom()
        else:
            print("\nI don't think that will work\n")
            hiddendoor()
    else:
        routines()
        hiddendoor()
    return

def keyroom():
    global movement
    global gold
    lightsource()
    probability()

    print("The only exit is to the east")

    if 'key' in keyroomfloor:
        print("Other than a large golden key in the center of the room, there is nothing else here")
    else:
        pass
    
    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("\nYou walk into a strange square cavern\n")
        hiddendoor()
    elif movement in TakeKeyVars:
        if CharName == "LINK":
            print("\nYou pick up the key and suddenly feel compelled to raise it above your head\nfor a second")
            sound.play()
            pyglet.app.run()
            print("You then place it in your inventory\n")
            keyroomfloor.remove('key')
            inventory.append('key')
            keyroom()
        else:
            print("\nYou pick up the key and place it in your inventory\n")
            keyroomfloor.remove('key')
            inventory.append('key')
            keyroom()
    else:
        routines()
        keyroom()
    return

def darkroom():
    global movement
    global gold
    global CharName
    lightsource()
    probability()

    if 'demon' in fightlist:
        if CharName == 'JOHNNY':
            print("\nNow is the time to rosin up your bow\n");time.sleep(1)
        elif CharName == 'FRODO':
            if 'sword' in inventory:
                print("\nYour sword begins glowing blue\n");time.sleep(1)
            else:
                pass
        elif CharName == 'BILBO':
            if 'sword' in inventory:
                print("\nYour sword begins glowing blue\n");time.sleep(1)
            else:
                pass
        else:
            pass

        print("\nUpon entering the room, you see something moving");time.sleep(1)
        print("A huge black demon was waiting for you in the shadows!");time.sleep(1)
        print("It charges towards you!");time.sleep(1)
        print("What will you do?\n")

        movement = input("\n>>")
        movement = movement.lower()
        cls()

        if movement in AttackVars:
            if CharName == 'ADMIN':
                print("\nWith one swing of the banhammer you annihilate the demon\n")
                fightlist.remove('demon')
                darkroom()
            else:
                if 'sword' in inventory:
                    print("\nYou attack the demon with your sword\nYour attack bounces off his hide");time.sleep(1)
                    print("You narrowly avoid the demon's attack\n");time.sleep(1)
                    print("The demon attempts to attack again, but he is off balance from his last attack\nWhat will you do?")

                    movement = input("\n>>")
                    movement = movement.lower()
                    cls()

                    if movement in AttackVars:
                        print("\nYou attack the demon again");time.sleep(1)
                        print("Although it doesn't hurt it, the demon is thrown further off balance");time.sleep(1)
                        print("It's underbelly is exposed, it looks vulnerable");time.sleep(1)
                        print("Now what?")

                        movement = input("\n>>")
                        movement = movement.lower()
                        cls()

                        if movement in AttackVars:
                            print("\nYou stab the demon and your sword passes");time.sleep(1)
                            print("Easily through it's heart, killing it immediately\n");time.sleep(1)  
                            fightlist.remove('demon')
                            darkroom()
                        else:
                            print("\nThe demon slashes at you");time.sleep(1)
                            print("nThe demon's claws pass through you like butter\nYou have been killed");time.sleep(1)
                            print("After a while the demon leaves and a grue wanders out of the shadows\n")
                            death()                           
                        

                    elif movement in PushVars:
                        print("You shove the demon, throwing it further off balance");time.sleep(1)
                        print("It's underbelly is exposed, it looks vulnerable");time.sleep(1)
                        print("Now what?")

                        movement = input("\n>>")
                        movement = movement.lower()
                        cls()
                        
                        if movement in AttackVars:
                            print("\nYou stab the demon and your sword passes");time.sleep(1)
                            print("Easily through it's heart, killing it immediately\n");time.sleep(1)  
                            fightlist.remove('demon')
                            darkroom()
                        else:
                            print("\nThe demon slashes at you");time.sleep(1)
                            print("nThe demon's claws pass through you like butter\nYou have been killed");time.sleep(1)
                            print("After a while the demon leaves and a grue wanders out of the shadows\n")
                            death()                        
                    else:
                        print("\nThe demon's claws pass through you like butter\nYou have been killed");time.sleep(1)
                        print("After a while the demon leaves and a grue wanders out of the shadows\n")
                        death()
                else:
                    print("You don't have anything to attack the demon with");time.sleep(1)
                    print("\nThe demon's claws pass through you like butter\nYou have been killed");time.sleep(1)
                    print("After a while the demon leaves and a grue wanders out of the shadows\n")
                    death()
        elif movement in WestVars:
            print("\nYou quickly flee from the room\nThe demon does not follow\n")
            mossypath()
        elif movement in FleeVars:
            print("\nYou quickly flee from the room\nThe demon does not follow\n")
            mossypath()
        else:
            print("\nThe demon's claws pass through you like butter\nYou have been killed");time.sleep(1)
            print("After a while the demon leaves and a grue wanders out of the shadows\n")
            death()
    else:
        print("The room's only exit is to the west")
        
        if 'box' in darkroomfloor:
            print("\nNow that the demon is gone, you are free to look around the room");time.sleep(1)
            print("You notice a gilded box in the corner of the room\n")
        else:
            pass

        movement = input("\n>>")
        movement = movement.lower()
        cls()

        if movement in WestVars:
            print("\nThere is moss growing all along the floor and walls of the cave\n")
            mossypath()
        elif movement in TakeBoxVars:
            if CharName == 'JOHNNY':
                print("\nIts true, you are the best");time.sleep(1)
                print("Inside the box you find a golden fiddle\n")
                darkroomfloor.remove('box')
                inventory.append('golden fiddle')
                darkroom()
            else:
                print("\nYou open the box and find a golden idol");time.sleep(1)
                print("If you ever do make it out of this, you will be very rich\n")
                darkroomfloor.remove('box')
                inventory.append('golden idol')
                darkroom()
        else:
            routines()
            darkroom()
    return


def goal():                                                         #This was the goal area in alpha.  Beta+ it isn't
    global movement
    global gold
    print("\nThere is a pathway to the south and a small building with\nA locked door in the center of the clearing\n")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SouthVars:
        print("\nThe trail leads into a thick pine forest")
        checkpointlight()
        pineforest()
    elif movement in UnlockDoor:
        if 'key' in inventory:
            print("\nYou unlock the door and enter the building\n")
            if 'box' in goalfloor:
                print("There is a box of gold inside, you take the contents")
                goalfloor.remove('box')
                gold = gold + 5
                goal()
        else:
            print("\nI don't think that will work\n")
            darkroom()
    else:
        routines()
        goal()    
    return




def bridge():
    global movement
    global gold

    lightsource()
    sunroutine()
    probability()
  
    print("\nThe bridge has exits to the north and south")


    if 'toll' not in bridgeguard:
        print("\nThere appears to be a man guarding the bridge\n");time.sleep(1)
        print("You must pay five gold coins to cross this bridge\n");time.sleep(1)
    else:
        if CharName == 'ARTHUR':
            print("\nThe guard is gone; you may pass\n");time.sleep(1)
        else:
            print("\nThere appears to be a man guarding the bridge\n");time.sleep(1)
            
    movement = input("\n>>")
    movement = movement.lower()
    cls()
    
    
    if movement in SouthVars:
        print("\nThe trail leads to the area you awoke")
        clock()
        startarea()
    elif movement in NorthVars:
        if 'toll' in bridgeguard:
            print("\nYou cross the bridge, trying not to look down, and step out into a field of clover");time.sleep(1)
            clock()
            cloverfield()
        else:
            print("\nYou must pay the guard in order to cross this bridge.");time.sleep(1)
            bridge()
    elif movement in PayVars:
        if CharName == 'ARTHUR':
            if 'guard' in bridgeguard:
                print("\nThe guard stops you and asks: 'What... is the average air-speed velocity of an unladen swallow?'");time.sleep(3)

                riddle = input("\n\n>>")

                if riddle in SwallowVars:
                    print("\nThe guard looks puzzled for a moment before being thrown from the edge\nof the cliff by an unseen force.");time.sleep(1)
                    bridgeguard.append('toll')
                    bridge()
                elif riddle in AnswerVars:
                    print("\nThat is correct. You may pass")
                    bridgegaurd.append('toll')
                    bridge()
                else:
                    if 'bag of gold' in inventory and 'toll' not in bridgeguard:
                        print("\n'Incorrect'\nYou reach into your bag and pull out a few gold pieces and hand them to the guard.");time.sleep(1.5)
                        bridgeguard.append('toll')
                        bridge()
                    elif 'golden fiddle' in inventory and 'toll' not in bridgeguard:
                        print("\n'Incorrect'\nYou must pay the toll.\nYou appologize for not having any gold with you.");time.sleep(2)
                        print("\nInstead, you show the guard the golden fiddle you took from the demon's lair.");time.sleep(2)
                        print("The guard gasps in surprise.\nHe seems impressed, and allows you to pass.");time.sleep(2)
                        bridgeguard.append('toll')
                        bridge()
                    elif 'toll' in bridgeguard:
                        print("\n'Incorrect' But you have already paid the toll. You don't need to pay twice.");time.sleep(1)
                        bridge()
                    else:
                        print("\n'Incorrect' You don't have any money with which to pay the guard.");time.sleep(1)
                        bridge()
            else:
                print("\nThe guard is gone; you may pass.");time.sleep(1)
        else:
            if gold >= 5 and 'toll' not in bridgeguard:
                print("\nYou reach into your bag and pull out a few gold pieces and hand them to the guard.");time.sleep(1.5)
                gold = gold - 5
                bridgeguard.append('toll')
                bridge()
            elif 'golden fiddle' in inventory and 'toll' not in bridgeguard:
                print("\nYou appologize for not having any gold with you.\nInstead, you show the guard the golden fiddle you took from the demon's lair.")
                print("The guard accepts the fiddle as payment");time.sleep(3)
                gold = gold - 5
                bridgeguard.append('toll')
                bridge()
            elif 'toll' in bridgeguard:
                print("\nYou have already paid the toll. You don't need to pay twice.");time.sleep(1)
                bridge()
            else:
                print("\nYou don't have any money with which to pay the guard.");time.sleep(1)
                bridge()
    elif movement in AttackVars:
        if 'sword' in inventory:
            attackguard = input("Are you sure you want to attack this man?\nHe looks dangerous.\n\n>>");time.sleep(1)
            if attackguard == 'yes':
                print("\nMid swing you change your mind and do not attack");time.sleep(1)
                bridge()
            else:
                print("\nThat's probably a good idea.");time.sleep(1)
                bridge()
        else:
            print("\nYou don't have anything to attack him with.");time.sleep(1)
            bridge()
    else:
        routines()
        bridge()
    return

def cornfield():
    global movement
    global gold
    global corncob
    lightsource()
    sunroutine()
    probability()

    print("\nYou are in a cornfield there is field of clover to the south and a large mountain to the east")
    
    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SouthVars:
        print("\nYou walk south into a field of clover.")
        clock()
        cloverfield()
    elif movement in CornVars:
        if corncob == 1:
            print("\nYou take a cob of corn from one of the stalks.");time.sleep(.5)
            inventory.append('corn cob')
            corncob = 0
            cornfield()
        else:
            print("\nSurely this corn belongs to someone, you shouldn't take it all!");time.sleep(1)
            cornfield()
    elif movement in EastVars:
        print("\nYou walk east along a winding path")
        clock()
        mountainpass()
    else:
        routines()
        cornfield()
    return

def cloverfield():
    global movement
    global gold
    global checkpoint
    lightsource()
    sunroutine()
    probability()

    if checkpoint == 0:                                    # checkpoints will come in handy for respawn and for other options
        checkpoint = 1
    else:
        pass


    print("\nThere is a cornfield to the north, a bridge to the south, and a winding path to the west")
            
    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SouthVars:
        print("\nYou walk back across the bridge.")
        clock()
        bridge()
    elif movement in NorthVars:
        print("\nYou walk into a large cornfield")
        clock()
        cornfield()
    elif movement in WestVars:
        print("The path leads down into the canyon")
        clock()
        canyon()
    elif movement in CloverSearchVars:
        foundclover = random.randint(1, 50)
        print("\nYou search for a four-leaf clover")
        if 'lucky clover' not in inventory:
            if foundclover == 40:
                print("\nYou found a four-leaf clover!");time.sleep(1.5)
                print("This will bring you good luck");time.sleep(1)
                print("You place the clover in your inventory")
                inventory.append('lucky clover')
                cloverfield()
            else:
                print("\nYou did not find a four-leaf clover")
                cloverfield()
        else:
            print("\nYou did not find a four-leaf clover")
            cloverfield()
    else:
        routines()
        cloverfield()
    return


def canyon():
    global movement
    global gold
    lightsource()
    sunroutine()
    probability()

    print("\nThere is a path to the east, west, and south")
    
    if 'rock' in manlocation:
        print("A large boulder is close to the northern canyon face")
    else:
        pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("\nYou walk east into a field of clover.")
        clock()
        cloverfield()
    elif movement in WestVars:
        print("\nYou come across a large body of water deep in the canyon")
        clock()
        canyonlake()
    elif movement in NorthVars:
       if 'rock' in manlocation:
           print("\nUpon looking closer, you notice a man stuck behind the rock"); time.sleep(.5)
           print("The rock cannot be moved from your side and he looks too week to move it himself"); time.sleep(.5)
           print("Maybe if you gave him some nourishment he could move it himself\n")
           canyon()
       else:
           print("\nI don't think that will work")
           canyon()
    elif movement == 'examnine rock' or 'check rock' or 'rock':
       if 'rock' in manlocation:
           print("\nUpon looking closer, you notice a man stuck behind the rock"); time.sleep(.5)
           print("The rock cannot be moved from your side and he looks too week to move it himself"); time.sleep(.5)
           print("Maybe if you gave him some nourishment he could move it himself\n")
           canyon()
       else:
           print("\nI don't think that will work")
           canyon()
    elif movement == 'give food' or 'feed man' or 'feed him' or 'give man food' or 'give the man food':
       if 'cooked corn' in inventory:
           inventory.remove('cooked corn')
           manlocation.remove('rock')
           print("\nAfter eating the corn the man regains his strength and heaves the rock"); time.sleep(.5)
           print("He thanks you for your kindness and gives you some gold")
           gold = gold + 15
           clock()
           canyon()
       elif 'cooked fish' in inventory:
           inventory.remove('cooked fish')
           manlocation.remove('rock')
           print("\nAfter eating the fish the man regains his strength and heaves the rock"); time.sleep(.5)
           print("He thanks you for your kindness and gives you some gold")
           gold = gold + 15
           clock()
           canyon()
       else:
           print("You don't have anything edible")
           canyon()
    elif movement == 'give corn' or 'feed corn' or 'give man corn' or 'feed man corn' or 'feed the man corn' or 'give the man corn':
       if 'cooked corn' in inventory:
           inventory.remove('cooked corn')
           manlocation.remove('rock')
           print("\nAfter eating the corn the man regains his strength and heaves the rock"); time.sleep(.5)
           print("He thanks you for your kindness and gives you some gold")
           gold = gold + 15
           clock()
           canyon()
       else:
           print("You don't have anything edible")
           canyon()
    elif movement == 'give fish' or 'feed fish' or 'give man fish' or 'feed man fish' or 'feed the man fish' or 'give the man fish':
       if 'cooked fish' in inventory:
           inventory.remove('cooked fish')
           manlocation.remove('rock')
           print("\nAfter eating the fish the man regains his strength and heaves the rock"); time.sleep(.5)
           print("He thanks you for your kindness and gives you some gold")
           gold = gold + 15
           clock()
           canyon()
       else:
           print("You don't have anything edible")
           canyon()
    elif movement in SouthVars:
        print("\nYou walk south down a winding pathway")
        paydoor()
    else:
        routines()
        canyon()
    return    


def canyonlake():
    global movement
    global gold
    lightsource()
    sunroutine()
    probability()
    #add swimming and fishing for food      make the fish at the other place have rare things

    print("\nThere is a deep lake")
    print("The path leads to the east")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("The path leads down into the canyon")
        clock()
        canyon()
    elif movement in FishVars:
        if 'fishing rod' in inventory:
            if 'raw fish' not in inventory:
                print("\nYou cast out your line and wait for a fish to bite");time.sleep(3)
                if 'lucky clover' in inventory:
                    clock()
                    catchfish = random.randint(1, 5)
                else:
                    catchfish = random.randint(1, 20)
                    clock()
                if catchfish == 5:
                    print("\nYou caught a fish!");time.sleep(1)
                    print("With the proper preperation, this could be quite tasty");time.sleep(1)
                    print("You place the fish in your inventory\n");time.sleep(1)
                    inventory.append('raw fish')
                    clock()
                    canyonlake()
                else:
                    print("\nYou did not catch a fish\n");time.sleep(.5)
                    clock()
                    canyonlake()
            else:
                print("\nYou already have a fish with you");time.sleep(.5)
                canyonlake()
        else:
            print("\nYou need a fishing rod to do that");time.sleep(.5)
            canyonlake()
    elif movement == 'swim' or 'go swimming' or 'dive':
        print("\nYou dive into the water for a swim");time.sleep(.5)
        clock()
        swimincanyonlake()
    else:
        routines()
        canyonlake()
    return

def swimincanyonlake():
    global movement
    global gold
    lightsource()
    sunroutine()
    probability()
    
    print("\nYou're swimming in the lake in the canyon")
    print("The shore is to the east")

    if 'gold' in canyonlakefloor:
        print("\nYou see something shimmering underwater")
    else:
        pass

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in EastVars:
        print("\nYou get out of the water and dry off")
        clock()
        canyonlake()
    elif movement in DiveVars:
        print("\nYou dive underwater and look for the shimmering object")
        if 'lucky clover' in inventory:
            foundobject = random.randint(1, 3)
        else:
            foundobject = random.randint(1, 10)
        if foundobject == 2:
            foundgold = random.randint(1, 20)
            print("\You found", foundgold, "gold coins")
            print("You place the coins in your inventory")
            canyonlakefloor.remove('gold')
            gold = gold + foundgold
            clock()
            swimincanyonlake()
        else:
            print("\nYou spend some time looking, but you don't find anything of interest")
            clock()
            swimincanyonlake()
    else:
        routines()
        swimincanyonlake()
    return


def mountainpass():
    global movement
    global gold
    global formalities
    lightsource()
    sunroutine()
    probability()

    print("\nA dwarven caravan is stopped along the roadside")
    print("The dwarves look sociable")

    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in SpeakVars:
        if formalities == 0:
            print("\nHello wanderer, my name is Urist Grizzledspade, I'm the leader of this band.");time.sleep(1)
            print("We are a merchant group that has only just begun our westward journey from the mountainhome");time.sleep(1)
            print("We would be willing to trade if you were so inclined")
            formalities = 1
        else:
            print("\nWe have goods to trade if you are so inclined")
        mountainpass()
    elif movement in TradeVars:
        print("\nThese are the goods we have for sale:")
        if 'batteries' in dwarfstore:
            print("Some Flashlight Batteries")
        else:
            pass
        if 'golden idol' in dwarfstore:
            print("A Golden Idol")
        else:
            pass
        if 'golden fiddle' in dwarfstore:
            print("A Fiddle Made of Solid Gold")
        else:
            pass
        if 'sword' in inventory:
            print("A Beautiful Elven Sword")
        else:
            pass
        timesleep(.5); print('(say "buy [item]" or "sell [item]" to negotiate a deal')
        mountainpass()
    elif movement in BuyBatteriesVars:
        print('\n"Batteries cost 5 gold, is that all right"')

        purchase = input("\n>>")
        purchase = movement.lower()
        cls()

        if purchase == 'yes' or 'y':
            if gold > 4:
                print("\nYou purchase some flashlight batteries")
                inventory.append('batteries')
                gold = gold - 5
            else:
                print('\n"I am sorry, but you cannot afford to purchase that"')
        else:
            if 'lucky clover' in inventory:
                print('"Alright, just for you the price will be 3 gold coins"')

                purchase = input("\n>>")
                purchase = movement.lower()
                cls()

                if purchase == 'yes' or 'okay' or 'y' or 'sure':
                    if gold > 2:
                        print("\nYou purchase some flashlight batteries")
                        inventory.append('batteries')
                        gold = gold - 3
                    else:
                        print('\n"I am sorry, but you cannot afford to purchase that"')
                else:
                    print('\n"Maybe you would rather sell us something?"')
        mountainpass()
    elif movement in SellSwordVars:
        if 'sword' in inventory:
            if 'lucky clover' in inventory:
                print('\n"We would be willing to give you 100 gold coins for that"')

                purchase = input("\n>>")
                purchase = movement.lower()
                cls()

                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('sword')
                    dwarfstore.append('sword')
                    gold = gold + 100
                else:
                    print('\n"Okay, suit yourself"')
            else:
                print('\n"We would be willing to give you 75 gold coins for that"')
                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('sword')
                    dwarfstore.append('sword')
                    gold = gold + 75
                else:
                    print('\n"Okay, suit yourself"')
        else:
            print("\nI don't think that will work")
        mountainpass()
    elif movement in BuySwordVars:
        if 'sword' in dwarfstore:
            print('\n"We would be willing to sell that for 125 gold coins"')

            purchase = input("\n>>")
            purchase = movement.lower()
            cls()
            
            if purchase == 'yes' or 'okay' or 'sure' or 'y':
                if gold > 124:
                    print("\nYou buy a sword")
                    inventory.append('sword')
                    dwarfstore.remove('sword')
                    gold = gold - 125
                else:
                    print('\n"I am sorry, but you cannot afford that"')
            else:
                print('\n"Okay, suit yourself"')
        else:
            print("\nI don't think that will work")
        mountainpass()
    elif movement in SellIdolVars:
        if 'golden idol' in inventory:
            if 'lucky clover' in inventory:
                print('\n"We would be willing to give you 250 gold coins for that"')

                purchase = input("\n>>")
                purchase = movement.lower()
                cls()

                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('golden idol')
                    dwarfstore.append('golden idol')
                    gold = gold + 250
                else:
                    print('\n"Okay, suit yourself"')
            else:
                print('\n"We would be willing to give you 200 gold coins for that"')
                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('golden idol')
                    dwarfstore.append('golden idol')
                    gold = gold + 200
                else:
                    print('\n"Okay, suit yourself"')
        else:
            print("\nI don't think that will work")
        mountainpass()
    elif movement in BuyIdolVars:
        if 'golden idol' in dwarfstore:
            print('\n"We would be willing to sell that for 300 gold coins"')

            purchase = input("\n>>")
            purchase = movement.lower()
            cls()

            if purchase == 'yes' or 'okay' or 'sure' or 'y':
                if gold > 299:
                    print("\nYou buy the golden idol")
                    inventory.append('golden idol')
                    dwarfstore.remove('golden idol')
                    gold = gold - 300
                else:
                    print('\n"I am sorry, but you cannot afford that"')
            else:
                print('\n"Okay, suit yourself"')
        else:
            print("\nI don't think that will work")
        mountainpass()
    elif movement in SellFiddleVars:
        if 'golden fiddle' in inventory:
            if 'lucky clover' in inventory:
                print('\n"We would be willing to give you 250 gold coins for that"')

                purchase = input("\n>>")
                purchase = movement.lower()
                cls()

                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('golden fiddle')
                    dwarfstore.append('golden fiddle')
                    gold = gold + 250
                else:
                    print('\n"Okay, suit yourself"')
            else:
                print('\n"We would be willing to give you 200 gold coins for that"')
                if purchase == 'yes' or 'okay' or 'sure' or 'y':
                    inventory.remove('golden fiddle')
                    dwarfstore.append('golden fiddle')
                    gold = gold + 200
                else:
                    print('\n"Okay, suit yourself"')
        else:
            print("I don't think that will work")
        mountainpass()
    elif movement in BuyFiddleVars:
        if 'golden fiddle' in dwarfstore:
            print('\n"We would be willing to sell that for 300 gold coins"')

            purchase = input("\n>>")
            purchase = movement.lower()
            cls()

            if purchase == 'yes' or 'okay' or 'sure' or 'y':
                if gold > 299:
                    print("\nYou buy the golden fiddle")
                    inventory.append('golden fiddle')
                    dwarfstore.remove('golden fiddle')
                    gold = gold - 300
                else:
                    print('\n"I am sorry, but you cannot afford that"')
            else:
                print('\n"Okay, suit yourself"')
        else:
            print("I don't think that will work")
        mountainpass()
    elif movement in WestVars:
        print("\nYou walk into a large cornfield")
        clock()
        cornfield()
    elif movement in EastVars:
        print("\nYou look eastward, in the distance you see large, ornate golden doors\nleading into the mountain.");time.sleep(1.5)
        print("It is probably best not to try the dwarves patience, you decide not to go that way")
        clock()
        mountainpass()
    else:
        routines()
        mountainpass()
    return

def paydoor():
    global movement
    global gold
    lightsource()
    sunroutine()
    probability()

    print("\nThere is a path to the north and one to the west")
    if 'toll' not in paydoorguard:
        print("A man blocks the eastern path")
    else:
        pass
    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in NorthVars:
        print("\nYou walk back into the canyon")
        clock()
        canyon()
    elif movement in EastVars:
        if 'toll' in paydoorguard:
            print("\nYou walk east past the man")
            clock()
            meethim()
        else:
            print("\nThe man blocks your way")
            paydoor()
    elif movement in AttackVars:
        print("\nThe man nimbly dodges your attack and knocks you unconscious without saying a word");time.sleep(1)
        print("It may be best to not try that again...");time.sleep(1)
        print("After a few hours, you wake up")
        clock()
        paydoor()
    elif movement in SpeakVars:
        print("\nThe man says that he will move for 300 gold pieces")
        clock()
        paydoor()
    elif movement in PayVars:
        if 'toll' not in paydoorguard:
            if gold > 299:
                print("\nYou pay the man 300 gold coins")
                gold = gold - 300
                paydoorguard.append('toll')
                clock()
                paydoor()
            else:
                print("\nYou cannot afford the fee")
                clock()
                paydoor()
        else:
            print("\nWhy would you want to pay the man twice?")
            paydoor()
    else:
        routines()
        paydoor()
    return

def meethim():
    global movement
    global gold
    global checkpoint
    lightsource()
    sunroutine()
    probability()

    print("\nThere is a paths to the east and west")
    if checkpoint == 1:
        print("\nA man dressed all in red is asleep under a tree nearby")
    else:
        pass  
    
    movement = input("\n>>")
    movement = movement.lower()
    cls()

    if movement in WestVars:
        print("\nYou walk back along the road the road the man was guarding")
        clock()
        paydoor()
    elif movement in EastVars:
        if checkpoint == 2:
            print("\nYou and the man dressed in red walk eastwards, as you talk the sky gets continually darker")
            endgame()
        else:
            print("\nMaybe you should do something else first?")
            clock()
            meethim()
    elif movement in InteractVars:
        print("\nThe man wakes up, he seems startled to see you");time.sleep(1)
        print(CharName, "is that you?");time.sleep(1)
        print("It is! I thought you were dead!");time.sleep(1)
        print("What happened to you?");time.sleep(2)
        print("You explain to him that you don't remember who you are or anything about yourself");time.sleep(2)
        print("I can explain everything to you along the way, I'm heading east")
        checkpoint = 2
        clock()
        meethim()
    else:
        routines()
        meethim()
    return

def endgame():
    global movement
    global gold
    global checkpoint

    print("\nIt is very dark outside, darker then the sky ever is normally");time.sleep(1)
    print("You turn to say something about that to the man");time.sleep(1)
    print("WHAM!");time.sleep(1)
    print("The man has hit you over the head with a rock");time.sleep(1)
    print("I left you for dead once before. This time, you are done");time.sleep(1)
    print("We were partners, adventurers,", CharName, "and Daras");time.sleep(1)
    print("We finished the job of a lifetime, and you wanted to retire");time.sleep(1)
    print("You took half your gold and tried to walk away");time.sleep(1)
    print("There was no way I could allow that, we made so much gold together");time.sleep(1)
    print("If you were quitting, then so was I, but I was taking all the gold");time.sleep(1)
    print("We'd had many adventurs, the two of us. I almost felt bad when I did it");time.sleep(1)
    print("Some days I even began to regret smashing you over the head with that mace");time.sleep(1)
    print("But here you are! And with some gold too! I wil be taking your", gold, "coins");time.sleep(1)
    print("As your vision blacks out Daras walks away");time.sleep(2)
    print("THE END");time.sleep(5)
    print("Feel free to continue though")

    movement = input("\n>>")
    startarea()
    return
    

#Thing for the lulz

print("\n\n\n                 ___  ___ _        _   __  _")
print("                 |  \/  |(_) _ __ (_) / _|(_)  ___  _   _  ___ ")
print("                 | |\/| || || '__|| || |_ | | / __|| | | |/ __|")
print("                 | |  | || || |   | ||  _|| || (__ | |_| |\__ \ ")
print("                 \_|  |_/|_||_|   |_||_|  |_| \___| \__,_||___/")

time.sleep(2)

print ("\n\n\n===============================================================================")
print ("=======================This has been brought to you============================")
print ("====================================by Alex Production, Co.====================")
print ("===============================================================================")


time.sleep(1)

while True:     #loops when dies
    intro()


#actual start
    print("\n\nNow that you've given yourself a name, you look"); time.sleep(2)
    print("around and notice trees all around the clearing."); time.sleep(2)

    startarea()
    break



# copyright Charles Chauncy 2013


