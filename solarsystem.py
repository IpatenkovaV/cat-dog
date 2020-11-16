import pygame, math
from pygame import *
from math import *
from pygame.draw import *

FPS = 50
WIDTH = HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 215, 0)
green = (0, 255, 0)
orange = (255, 0, 255)
white = (255, 105, 180)
gray = (240, 230, 140)
BLACK = (0, 0, 0)
COLORS = [red, blue, yellow, green, orange, white, gray, BLACK]
X0=WIDTH/2
Y0=HEIGHT/2
A = 149.6*10**9
G = 6.57*10**(-11)




x_planet = [] 
y_planet = []
vy_planet = []
vx_planet =[]
color_planet = []
r_planet = []
m_planet = []
flag_obj = 0




'''input_filename = input("Введите название файла: ")'''
with open('solar_system.txt') as input_file:
    for line in input_file:
        if len(line.strip()) == 0 or line[0] == '#':
            continue  # пустые строки и строки-комментарии пропускаем

        tokens = line.split()
        assert(len(tokens) == 8)
        r_planet.append(int(tokens[1]))
        color_planet.append(tokens[2])
        m_planet.append(float(tokens[3]))
        x_planet.append(float(tokens[4]))
        y_planet.append(float(tokens[5]))
        vx_planet.append(float(tokens[6]))
        vy_planet.append(float(tokens[7]))
        flag_obj += 1

print(x_planet)

def change_coords(coords, scale):
	x = int(coords[0]*scale + X0)
	y = int(Y0 - coords[1]*scale)
	return (x,y)


def getScale(planets):
	maxPos = max([max(p.x, p.y) for p in planets])
	scale = min(WIDTH, HEIGHT)/(2*maxPos)
	return 0.8*scale


class Planet():
	def __init__(self, x, y, vx, vy, color, r, m=0):
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
		self.ax=0.0
		self.ay=0.0
		self.color = color
		self.r = r
		self.m = m

	def move(self, dt=1):	   
		#New pos based on speed
		self.x += self.vx*dt
		self.y += self.vy*dt

	def getPos(self):
		R = sqrt((self.x - 0)**2 + (self.y - 0)**2)
		return R

	def getMass(self):
		return self.m

def draw(obj, scale):
	screen_coords = change_coords((obj.x, obj.y), scale)
	circle(screen, obj.color, screen_coords, obj.r)


def gravitate(obj1, obj2, dt=1):
	R = sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
	print(obj1.x, obj2.x)	
	obj1.ax = G * obj2.getMass() * (obj2.x - obj1.x) / R**3
	obj1.ay = G * obj2.getMass() * (obj2.y - obj1.y) / R**3

	obj1.vx += obj1.ax*dt
	obj1.vy += obj1.ay*dt


clock = pygame.time.Clock()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
screen.fill(BLACK)

#Sun mass
M0 = 2*10**30
#Stop conditions
CRASH_DIST = 10
DT = 3600*24*3


planets = []
for i in range(flag_obj):
	x = x_planet[i]
	y = y_planet[i]   
	vx= vx_planet[i]
	vy = vy_planet[i]
	color = color_planet[i]
	r = r_planet[i]
	m = m_planet[i]
	planets.append(Planet(x, y, vx, vy, color, r//4, m))
Scale = getScale(planets)

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	i = 0
	while i < len(planets):
		p = planets[i]
		if i > 0:
			p.move(DT)
			R = p.getPos()

		for p2 in planets:
			if p != p2:
				gravitate(p, p2, DT)
		draw(p, Scale)

		if i>0 and (R < CRASH_DIST):
			planets.pop(i)
		else:
			i+=1
	pygame.display.update()
	screen.fill(BLACK)
	
	if R < CRASH_DIST:
		finished = True
		print("Crashed")
			
