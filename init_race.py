#############################################
#### ALL INITIALIZATION FOR RACE WINDOW #####
#############################################
racing_track = 'oval' # 'oval' or 'polar'
#############################################
import pygame
from configparser import SafeConfigParser
from PIL import Image
from random import randint
import utils

# for original track
if racing_track == 'oval':
    rewardgate1 = utils.rewardgates(460,510,10,100)#1
    rewardgate2 = utils.rewardgates(250,510,10,100)#2
    rewardgate3 = utils.rewardgates(25,510,175,10)#3
    rewardgate4 = utils.rewardgates(0,400,150,10)#4
    rewardgate5 = utils.rewardgates(25,265,155,10)#5
    rewardgate6 = utils.rewardgates(250,170,10,100)#6
    rewardgate7 = utils.rewardgates(460,170,10,100)#7
    rewardgate8 = utils.rewardgates(660,170,10,100)#8
    rewardgate9 = utils.rewardgates(860,170,10,100)#9
    rewardgate10 = utils.rewardgates(1070,170,10,100)#10
    rewardgate11 = utils.rewardgates(1150,265,110,10)#11
    rewardgate12 = utils.rewardgates(1170,400,155,10)#12
    rewardgate13 = utils.rewardgates(1120,510,145,10)#13
    rewardgate14 = utils.rewardgates(1070,510,10,100)#14
    rewardgate15 = utils.rewardgates(860,510,10,100)#15
    rewardgate16 = utils.rewardgates(660,510,10,100)#16
    init_pos = [(450,530,90,'gate1'),(230,530,90,'gate2'),(55,490,0,'gate3'),(30,390,0,'gate4'),(55,255,0,'gate5'),(260,200,270,'gate6'),(480,200,270,'gate7'),(680,200,270,'gate8'),(880,200,270,'gate9'),(1090,200,270,'gate10'),(1180,285,180,'gate11'),(1200,420,180,'gate12'),(1150,530,180,'gate13'),(1050,530,90,'gate14'),(840,530,90,'gate15'),(640,530,90,'start')]
#for polar bear track
elif racing_track == 'polar':
    rewardgate1 = utils.rewardgates(150,400,150,10)#1
    rewardgate2 = utils.rewardgates(190,265,155,10)#2
    rewardgate3 = utils.rewardgates(410,120,10,110)#3
    rewardgate4 = utils.rewardgates(590,90,10,90)#4
    rewardgate5 = utils.rewardgates(750,60,10,100)#5
    rewardgate6 = utils.rewardgates(960,80,10,70)#6
    rewardgate7 = utils.rewardgates(1070,190,125,10)#7
    rewardgate8 = utils.rewardgates(950,230,10,80)#8
    rewardgate9 = utils.rewardgates(1030,365,10,90)#9
    rewardgate10 = utils.rewardgates(1050,460,165,10)#10
    rewardgate11 = utils.rewardgates(1030,485,10,80)#11
    rewardgate12 = utils.rewardgates(760,365,10,100)#12
    rewardgate13 = utils.rewardgates(550,440,85,10)#13
    rewardgate14 = utils.rewardgates(510,550,10,120)#14
    rewardgate15 = utils.rewardgates(380,530,10,130)#15
    rewardgate16 = utils.rewardgates(180,510,175,10)#16
    init_pos = [(225,410,0,'gate1'),(252,275,0,'gate2'),(390,175,270,'gate3'),(580,135,270,'gate4'),(740,110,270,'gate5'),(950,115,270,'gate6'),(1135,180,180,'gate7'),(960,270,90,'gate8'),(1020,410,270,'gate9'),(1130,450,180,'gate10'),(1040,525,90,'gate11'),(770,415,45,'gate12'),(590,430,180,'gate13'),(520,610,90,'gate14'),(390,595,90,'gate15'),(268,520,0,'start')]


#Settin' up the window!
pygame.init()
pygame.font.init()
fontbig = pygame.font.Font("res/Saira-Regular.ttf", 100)
font = pygame.font.Font("res/Saira-Regular.ttf", 20)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 5")
pygame.display.flip()

#Re-collecting those settings!
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
carimagepath2 = parser.get("options", "carimage2")
trackstring = parser.get("options", "track")
#trackpath = parser.get("options", "trackpath")
if racing_track == 'oval': 
    trackpath = "res/Original.png"
else:
    trackpath = "res/PolarBear Roundoff_upscaled.png"
shifting = parser.get("options", "shifting")
shifting2 = parser.get("options", "shifting2")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    #screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1280, 720))
players = parser.get("options", "players")
trackimage = pygame.image.load(trackpath)
track = int(trackstring)
trackkey = "track" + str(track)
car = parser.get("options", "car")
car2 = parser.get("options", "car2")
clockspeedstring = parser.get("options", "speed")
playername = parser.get("options", "name")
showstartcountdown = parser.get("options", "showstartcountdown")
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
tim = Image.open(trackpath)
trackpil = tim.load()

#Variables
carimage = pygame.image.load(carimagepath)
carimage3 = pygame.image.load(carimagepath2)
clock = pygame.time.Clock()
x = 30
y = 30
nos = 0
nosinuse = False
nosinuse2 = False
lap = "Lap: "
lapcount = 0
lapcount2 = 0
place = 11
atstart = True
atstart2 = True
newlap = False
newlap2 = False
laptime = 0
score = 0
enginecounter = 0
enginecounter2 = 0
Up = "Up"
Down = "Down"
Left = "Left"
Right = "Right"
LeftUp = "LeftUp"
LeftDown = "LeftDown"
RightUp = "RightUp"
RightDown = "RightDown"
lastdirection = Down
finished = False
checklap = False
checklap2 = False
lapcheck2 = False
lapcheck = False


#Colours (Thanks to atmatm6 for the code in this section!)
black = (0,0,0)
white = (255,255,255)
brown = (100,42,42)
gray = (128,128,128)
darkdarkred = (64,0,0)
rhubarb = (128,0,0)
red = (255,0,0)
redorange = (255,64,0)
orange = (255,128,0)
orangeyellow = (255,192,0)
yellow = (255,255,0)
limegreen = (192,255,0)
screengreen = (128,255,0)
lightgreen = (64,255,0)
green = (0,255,0)
mehgreen = (0,255,64)
greenblue = (0,255,128)
aqua = (0,255,192)
lightblue = (0,255,255)
turquoise = (0,192,255)
teal = (0,128,255)
lightdarkblue = (0,64,255)
blue = (0,0,255)
darkblue = (64,0,255)
purple = (128,0,255)
violet = (192,0,255)
magenta = (255,0,255)
darklightmagenta = (255,0,192)
pink = (255,0,128)
lightred = (255,0,64)

#Get all stats from the ini files
parser.read("res/carstats.ini")
carspeed = parser.get(car, "speed")
caraccel = parser.get(car, "accel")
carbrake = parser.get(car, "brake")
carhandling = parser.get(car, "handling")
carbrake = parser.get(car, "brake")
caraero = parser.get(car, "aero")
carnos = parser.get(car, "nos")
carspeed2 = parser.get(car2, "speed")
caraccel2 = parser.get(car2, "accel")
carbrake2 = parser.get(car2, "brake")
carhandling2 = parser.get(car2, "handling")
carbrake2 = parser.get(car2, "brake")
caraero2 = parser.get(car2, "aero")
carnos2 = parser.get(car2, "nos")
parser.read("res/tracks.ini")
maxlap = int(parser.get(trackkey, "laps"))
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")
checkpointy2 = parser.get(trackkey, "checkpointy2")
checkpointx2 = parser.get(trackkey, "checkpointx2")
checkpointy3 = parser.get(trackkey, "checkpointy3")
checkpointx3 = parser.get(trackkey, "checkpointx3")
parser.read("res/highscore.ini")
p1 = int(parser.get(trackkey, "1"))
p2 = int(parser.get(trackkey, "2"))
p3 = int(parser.get(trackkey, "3"))
p4 = int(parser.get(trackkey, "4"))
p5 = int(parser.get(trackkey, "5"))
p6 = int(parser.get(trackkey, "6"))
p7 = int(parser.get(trackkey, "7"))
p8 = int(parser.get(trackkey, "8"))
p9 = int(parser.get(trackkey, "9"))
p10 = parser.get(trackkey, "10")
p10 = int(p10)
p1 = randint(-1 , 99) + p1
p2 = randint(-1 , 99) + p2
p3 = randint(-1 , 99) + p3
p4 = randint(-1, 99) + p4
p5 = randint(-1 , 99) + p5
p6 = randint(-1, 99) + p6
p7 = randint(-1 , 99) + p7
p8 = randint(-1 , 99) + p8
p9 = randint(-1 , 99) + p9
p10 = randint(-1 , 99) + p10
pixcoloour = (0,0,0)
changetr = 0

#More Variables!!!!
mostnos = int(carnos)
nosleft = int(carnos)
aero = int(caraero) / 10
cartopspeed = int(carspeed) / 18 * aero
topspeed = int(carspeed) / 18 * aero
braking = int(carbrake) / 500 * aero
accel = int(caraccel) / 2100 * aero
handling = int(carhandling) / 30 * aero
righthandling = 360 - handling
mostnos2 = int(carnos2)
nosleft2 = int(carnos2)
aero2 = int(caraero2) / 10
cartopspeed2 = int(carspeed2) / 18 * aero2
topspeed2 = int(carspeed2) / 18 * aero2
braking2 = int(carbrake2) / 500 * aero2
accel2 = int(caraccel2) / 2100 * aero2
handling2 = int(carhandling2) / 30 * aero2
righthandling2 = 360 - handling2
curspeed = 0
startlinex = int(startx)
startliney = int(starty)
checky = int(checkpointy)
checkx = int(checkpointx)
checky2 = int(checkpointy2)
checkx2 = int(checkpointx2)
checky3 = int(checkpointy3)
checkx3 = int(checkpointx3)
checkplus40x = checkx + 80
checkminus40x = checkx - 80
checkplus40y = checky + 80
checkminus40y = checky - 80
checkplus40x2 = checkx2 + 80
checkminus40x2 = checkx2 - 80
checkplus40y2 = checky2 + 80
checkminus40y2 = checky2 - 80
checkplus40x3 = checkx3 + 80
checkminus40x3 = checkx3 - 80
checkplus40y3 = checky3 + 80
checkminus40y3 = checky3 - 80
if trackkey == "track8":
    checkplus40x = checkx + 120
    checkminus40x = checkx - 120
    checkplus40y = checky + 120
    checkminus40y = checky - 120
    checkplus40x2 = checkx2 + 120
    checkminus40x2 = checkx2 - 120
    checkplus40y2 = checky2 + 120
    checkminus40y2 = checky2 - 120
    checkplus40x3 = checkx3 + 200
    checkminus40x3 = checkx3 - 200
    checkplus40y3 = checky3 + 200
    checkminus40y3 = checky3 - 200
x = startliney
y = startlinex
y2 = startlinex - 10
x2 = startliney
if trackkey != "track4":
    if trackkey != "track3":
        if trackkey != "track6":
            if trackkey != "track7":
                x2 = startliney - 61
                y2 = startlinex
if trackkey == "track8":
    x2 = startliney + 55
startneg80x = startlinex - 80
if trackkey != "track4":
    if trackkey != "track3":
        if trackkey != "track6":
            if trackkey != "track7":
                startneg80x = startlinex
gol = fontbig.render("Go!", 10, white)
start80x = startlinex + 80
passstart = startliney + 10
rotater = 0
gear = 1
gear2 = 1
rotater2 = 0
carimage2 = pygame.transform.rotate(carimage, 0)
carimage4 = pygame.transform.rotate(carimage3, 0)
if trackkey == "track3" :
    carimage2 = pygame.transform.rotate(carimage, 90)
    rotater = 90
    carimage4 = pygame.transform.rotate(carimage3, 90)
    rotater2 = 90
    passstart = startlinex - 10
if trackkey == "track4" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
if trackkey == "track6" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
if trackkey == "track7" :
    carimage2 = pygame.transform.rotate(carimage, 270)
    rotater = 270
    carimage4 = pygame.transform.rotate(carimage3, 270)
    rotater2 = 270
    passstart = startlinex - 10
    y -= 30
    nosleft = 0
    nosleft2 = 0
if trackkey == "track5":
    cartopspeed2 = int(carspeed2) / 10 * aero2
    topspeed2 = int(carspeed2) / 10 * aero2
    cartopspeed = int(carspeed) / 10 * aero
    topspeed = int(carspeed) / 10 * aero
pos = 0
togo = 0
maxlaps = maxlap + 1
score = 0
pos2 = 0
togo2 = 0
maxlaps2 = maxlap + 1
score2 = 0
trackkey2 = trackkey
curspeed2 = 0
rot2 = 0
racestartbol = True

#Passoff to the postrace Python script
def sendtopost():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global score
    global place
    global trackkey
    global score2
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global gol
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "racefinsihed", "Yes")
    parser.set("options", "score", str(score))
    parser.set("options", "place", str(place))
    parser.set("options", "score2", str(score2))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    parser.read("res/highscore.ini")
    parser.set(trackkey, "p1", str(p1))
    parser.set(trackkey, "p2", str(p2))
    parser.set(trackkey, "p3", str(p3))
    parser.set(trackkey, "p4", str(p4))
    parser.set(trackkey, "p5", str(p5))
    parser.set(trackkey, "p6", str(p6))
    parser.set(trackkey, "p7", str(p7))
    parser.set(trackkey, "p8", str(p8))
    parser.set(trackkey, "p9", str(p9))
    parser.set(trackkey, "p10", str(p10))
    with open('res/highscore.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("prepostrace.py").read())


