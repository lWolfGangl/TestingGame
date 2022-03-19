
from SickDogM import SickDog
from TreasureMod import Treasure
from Enemies import Enemy
from PerreroM import Perrero
import pygame
from turtle import forward, right, onkeypress, listen, bye, done
import turtle
import time
import math
import random
import PlayerPerro
import TreasureMod
import TrapMod
import Enemies
import SickDogM
import flags
import PerreroM



delay = 0.1
wn = turtle.Screen()
wn.bgcolor("#BDBDBD")
wn.title("dungeon")
wn.setup(605,605)
wn.tracer(0)

#Register Shapes
turtle.register_shape("../img/crazydog.gif")
turtle.register_shape("../img/pared.gif")
turtle.register_shape("../img/ninio.gif")
#turtle.register_shape("dog.gif")
#turtle.register_shape("dog_left.gif")
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

#marker

 
Level=1
walls = []
enemywalls=[]
flagsarray=[]
traps=[]  
ninios=[]
cazadores = []
treasures = []
crazydogs=[]
enemies = []
levels = [""]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X          P            X",
"X                       X",
"X                   T   X",
"XXXXXNNNNNNNNNNNNNNNXXXXX",
"XXXXX   T O         XXXXX",
"XXXXXNNNNNNNNNNNNNNNXXXXX",
"XXXXXXXXX       XXXXXXXXX",
"X                       X",
"X          E            X",
"X                     O X",
"XXXXXXXXXXXXXXXXXXXXXNNNX",
"XXXXXXXXXXXXXXXXXXXXXNNNX",
"X          N            X",
"X                       X",
"X   O                   X",
"XN        C N         T X",
"X                       X",
"X               O       X",
"X T                 NT  X",
"XNNNXXXXXXXXXXXXXXXXXXXXX",
"X  OXXXXXXXXXXXXXXXXXXXXX",
"X   XXXXXXXXXXXXXXXXXXXXX", 
"X                      FX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP   XT          E      X",
"X    XO             X   X",
"X    N    XXXXXX    XT  X",
"XXXXXXXXXXXTNNNNONNNNXXXXX",
"XE                      X",
"X     T                 X",
"X            XXXXXXXXXXXX",
"X          EXT         CX",
"XNNNNNXXXXXXX O         X",
"X     X                 X",
"XO             E        X",
"XT  X                   X",
"XXXXX                   X",
"XXXXXXXXXXXXXX          X",
"XXXXXXXXXXXXXXXXXXXXNNNNX",
"XT     EX               X",
"X       X               X",
"X       XC              X",
"X       X               X",
"X       N            XXXX",
"X       N TXXXXXXXXXXXXXX",
"XNNNNNXXXXXXXXXXXXXXXXXXX",                
"X                      FX",    
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                     TX",
"XNNOXXXXXXXXXXXXXXXXXXXXX",
"X            O         TX",
"XXXXXXXXXXE      XXXXXNNX",
"XXXXXXXXXXXXXXXXXXXXXXNNX",
"X                       X",
"X                       X",
"XNNNNXXXXXXXXXXXXXXXXXXXX",
"X              N     T  X",
"X   C                   X",
"X     N        E        X",
"XXXXXXXXXXXXXXXXXXXXNNNNX",
"XXXXXXXXXXXXXXXXXXXX    X",
"XXXXXXXXXXXXXXXXXXXX    X",
"XXXXXXXXXXXXXXXXXXXXNNNNX",
"XT        N          O  X",
"X    OT                 X",
"X        S              X",
"X T             N  OT   X",
"XNNNXXXXXXXXXXXXXXXXXXXXX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"XNNNXXXXXXXXXXXXXXXXXXXXX",                
"XOT                    FX",    
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XT                     PX",
"XNNOXXXXXXXXXXXXXXXXXXXXX",
"X            O         TX",
"XNNXXXXXXXE      XXXXXNNX",
"XNNXXXXXXXXXXXXXXXXXXXNNX",
"X                       X",
"X                       X",
"XXXXXXXXXXNNNNNXXXXXXXXXX",
"X              N     T  X",
"X   C                   X",
"X     N        E        X",
"XXXXXXXXXXXXXXXXXXXXNNNNX",
"XXXXXXXXXXXXXXXXXXXX    X",
"XXXXXXXXXXXXXXXXXXXX    X",
"XXXXXXXXXXXXXXXXXXXXNNNNX",
"XT        N          O  X",
"X    OT                 X",
"X        S              X",
"X T             N  OT   X",
"XNNNXXXXXXXXXXXXXXXXXXXNX",
"X   XXXXXXXXXXXXXXXXXXXNX",
"XNNNXXXXXXXXXXXXXXXXXXXNX",                
"XOT                    BX",    
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
pen = Pen()

def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			character = level[y][x]
			screen_x = -288 + (x*24)
			screen_y = 288 - (y*24)
			if character == 'X':
				pen.goto(screen_x, screen_y)
				pen.shape("../img/pared.gif")
				pen.stamp()
				walls.append((screen_x, screen_y))
			if character == 'N':
				enemywalls.append((screen_x, screen_y))
			if character == 'P':
				player.goto(screen_x, screen_y)

			if character == 'T':
				treasures.append(TreasureMod.Treasure(screen_x, screen_y))

			if character == 'O':
				traps.append(TrapMod.Trap(screen_x, screen_y))

			if character == 'E':
				enemies.append(Enemies.Enemy(walls,enemywalls, screen_x, screen_y))
			if character == 'C':
				crazydogs.append(SickDogM.SickDog(walls,enemywalls, screen_x, screen_y))
			if character == 'F':
				flagsarray.append(flags.Flag(screen_x, screen_y))
			if character == 'S':
				cazadores.append(PerreroM.Perrero(walls, enemywalls,screen_x, screen_y))
			if character == 'B':
				pen.goto(screen_x, screen_y)
				pen.shape("../img/ninio.gif")
				pen.stamp()
				ninios.append((screen_x, screen_y))

def reset_maze(level):
	pen.clearstamps()
	walls.clear()
	for treasure in treasures:
		treasure.destroy()

	for Trap in traps:
		Trap.destroy()
	for enemy in enemies:
		enemy.destroy()
	for sickdog in crazydogs:
		sickdog.destroy()
	enemywalls.clear()
	flagsarray.clear()
	traps.clear()
	treasures.clear()
	crazydogs.clear()
	enemies.clear()
	cazadores.clear()

def ultimo_nivel():
	oro=format(player.gold)
	print(oro)
	palabra=""
	palabra=str(oro)
	ventana = pygame.display.set_mode((ANCHO,ALTO))
	reloj = pygame.time.Clock()
	fuente1 = pygame.font.SysFont("arial black", 24)
	fuente2 = pygame.font.SysFont("Segoe print", 32)
	player.dies()
	for i in range(0,2500):
		ventana.fill(NEGRO)
		potente = [
			"OH VAYA, QUIEN ESTÁ AHÍ?",
			"ES TU DUEÑO, CARLO CORRALES",
			"ALCANZALO PARA LLEGAR A CASA",
			"PUNTUACION "+palabra,
			"",
			"CARGANDO SIGUIENTE NIVEL..."
			]
		z = 80
		for frase in potente:
			texto = fuente2.render(frase, True, BLANCO)
			ventana.blit(texto,(150,z))		
			z += 80
		pygame.display.update()

def ganaste():
	oro=format(player.gold)
	print(oro)
	palabra=""
	palabra=str(oro)
	ventana = pygame.display.set_mode((ANCHO,ALTO))
	reloj = pygame.time.Clock()
	fuente1 = pygame.font.SysFont("arial black", 24)
	fuente2 = pygame.font.SysFont("Segoe print", 32)
	bg = pygame.image.load("../img/nuevofondofinal.png")
	player.dies()
	for r in range(0,2500):
		ventana.fill(NEGRO)
		#bg = pygame.image.load("../img/fotofelices.png")

		#INSIDE OF THE GAME LOOP
		ventana.blit(bg, (0, 0))
		perdida = [
			"GANASTE:",
			"LLEGASTE CON TU DUEÑO",
			"PUNTUACION "+palabra,
			"",
			"FELICIDADES!!!"
			]
		z = 80
		for frase in perdida:
			texto = fuente2.render(frase, True, BLANCO)
			ventana.blit(texto,(150,z))		
			z += 80
		wn.delay(0)
		pygame.display.update()
	wn.bye()

def findeljuego():
	player.dies()
	oro=format(player.gold)
	print(oro)
	palabra=""
	palabra=str(oro)
	ventana = pygame.display.set_mode((ANCHO,ALTO))
	reloj = pygame.time.Clock()
	fuente1 = pygame.font.SysFont("arial black", 24)
	fuente2 = pygame.font.SysFont("Segoe print", 32)
	player.dies()
	for i in range(0,2500):
		ventana.fill(NEGRO)
		perdida = [
			"PERDISTE",
			"PUNTUACION "+palabra,
			"",
			"NO TE RINDAS!!"
			]
		z = 80
		for frase in perdida:
			texto = fuente2.render(frase, True, BLANCO)
			ventana.blit(texto,(150,z))		
			z += 80
		pygame.display.update()
	wn.bye()
def animate_entities():
	for enemy in enemies:
		enemy.move()
	for sickdog in crazydogs:
		sickdog.move()
	for cazador in cazadores:
		cazador.move()


player = PlayerPerro.Player(walls)
setup_maze(level_1)

# keybindings
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

pygame.init()

ANCHO = 1280
ALTO = 720

BLANCO = (255,255,255)
NEGRO = (0,0,0)

ventana = pygame.display.set_mode((ANCHO,ALTO))
reloj = pygame.time.Clock()
fuente1 = pygame.font.SysFont("arial black", 24)
fuente2 = pygame.font.SysFont("Segoe print", 32)

en_juego = True
en_partida = False
en_display = False
en_vivo = True

for enemy in enemies:
	turtle.ontimer(enemy.move, t=250)

for sickdog in crazydogs:
	turtle.ontimer(sickdog.move, t=250)

while en_juego:

	en_partida = False
	en_inicio = True

	while en_inicio:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				en_inicio = False
				en_juego = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					en_inicio = False
					en_partida = True
					

		ventana.fill(NEGRO)

		historia = [
			"MISION REGRESA A CASA:",
			"UN DIA BOLT SE PUSO A JUGAR CON SU PELOTA",
			"Y SU DUEÑO ABRIÓ LA PUERTA DEL GARAGE",
			"Y BOLT SE ESCAPÓ PENSANDO QUE ERA UN JUEGO",
			"AHORA BOLT NO SABE COMO REGRESAR A CASA",
			"Y ESTÁ MUY ASUSTADO AYÚDALO A REGRESAR A CASA",
			"",
			"PULSA 'ENTER' PARA EMPEZAR"
		]
		y = 80
		for frase in historia:
			texto = fuente2.render(frase, True, BLANCO)
			ventana.blit(texto,(150,y))
			y += 80
		pygame.display.update()
		
	while en_partida:
		pygame.display.quit()
		if (Level==1 and (player.xcor()==264 and player.ycor()==-264)):
			reset_maze(level_2)
			setup_maze(level_2)
			animate_entities()
			Level=2
		if (Level==2 and (player.xcor()==264 and player.ycor()==-264)):
			#ultimo_nivel()
			reset_maze(level_3)
			setup_maze(level_3)
			animate_entities()
			Level=3
		if (Level==3 and (player.xcor()==264 and player.ycor()==-264)):
			ultimo_nivel()
			reset_maze(level_4)
			setup_maze(level_4)
			animate_entities()
			Level=4
		if (Level==4 and (player.xcor()==264 and player.ycor()==-264)):
			ganaste()

		for treasure in treasures:
			if player.is_collision(treasure):
				player.gold += treasure.gold
				print ("Player Gold: {}".format(player.gold))
				treasure.destroy()
				treasures.remove(treasure)
		for Trap in traps:
			if player.is_collision(Trap):
				findeljuego()
				
		for enemy in enemies:
			if player.is_collision(enemy):
				findeljuego()
		for sickdog in crazydogs:
			sickdog.atackPlayer(player)
			if player.is_collision(sickdog):
				findeljuego()
		for cazador in cazadores:
			cazador.atackPlayer(player)
			if player.is_collision(cazador):
				findeljuego()
		wn.update()
