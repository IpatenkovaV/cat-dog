import pygame, math
from pygame import *
from math import *
from pygame.draw import *

FPS = 50
WIDTH = 1400
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PINK = (255, 105, 180)
KHAKI = (240, 230, 140)
CYAN = (0, 255, 255)
SIENNA = (160, 82, 45)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, PINK, KHAKI, CYAN, SIENNA, BLACK]
X0=WIDTH/2
Y0=HEIGHT/2
A = 149.6*10**9
G = 6.57*10**(-11)

x_planet= [0.387 * A, 0.723 * A, 1 * A, 1.52 * A, 5.2 * A, 9.54 * A, 19.2 * A, 30 * A] 
y_planet= [0]*8
vy_planet = [47870, 35020, 29780, 24130, 13070, 9690, 6810, 5430]
vx_planet=[0, 0, 0, 0, 0, 0, 0, 0]
color_planet = [RED, BLUE, GREEN, MAGENTA, PINK, KHAKI, CYAN, SIENNA]
r_planet = [4, 9, 10, 5, 112, 94, 40, 39]
m_planet = [3.3*10**23, 4.87*10**24, 5.976*10**24, 6.48*10**23, 1.9*10**27, 5.68*10**26, 8,7*10**25, 1*10**26]

def change_coords(coords, scale):
	x = coords[0]*scale + X0
	y = Y0 - coords[1]*scale
	return (x,y)


def getScale(planets):
	maxPos = max([max(p.x, p.y) for p in planets])
	scale = max(WIDTH, HEIGHT)/(2*maxPos)
	return 0.9*scale


class Planet():
	def __init__(self, x, y, vx, vy, color, r, m=0):
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
		self.ax=0
		self.ay=0
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


def make_sun(M0):
	sun = Planet(0, 0, 0, 0, YELLOW, 5)
	sun.m = M0
	return sun

def gravitate(obj1, obj2, dt=1):
	R = sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
		
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

Sun = make_sun(M0) 
planets = []
planets.append(Sun)
for i in range(8):
	x = x_planet[i]
	y = y_planet[i]   
	vx= vx_planet[i]
	vy = vy_planet[i]
	color = color_planet[i]
	r = r_planet[i]
	m = m_planet[i]
	planets.append(Planet(x, y, vx, vy, color, r/4, m))
Scale = getScale(planets)

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	i = 0
	while (i < len(planets)):
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


