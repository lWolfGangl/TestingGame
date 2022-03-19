import sys 
sys.path.append("../entities")
from PlayerPerro import Player
from Enemies import Enemy
from SickDogM import SickDog
from TrapMod import Trap
from TreasureMod import Treasure
from PerreroM import Perrero
from flags import Flag
import unittest
import math

#verifica que el jugador se pueda mover con las teclas
def test_player_go_right():
    player = Player (walls)
    ant_posx,ant_posy = player.xcor(), player.ycor()
    Player.go_right(player)
    posx , posy = player.xcor(), player.ycor()
    assert (posx-ant_posx==24 and posy==ant_posy)
    del player

def test_player_go_left():
    player = Player (walls)
    ant_posx,ant_posy = player.xcor(), player.ycor()
    Player.go_left(player)
    posx , posy = player.xcor(), player.ycor()
    assert (posx-ant_posx==-24 and posy==ant_posy)
    del player

def test_player_go_up():
    player = Player (walls)
    ant_posx,ant_posy = player.xcor(), player.ycor()
    Player.go_up(player)
    posx , posy = player.xcor(), player.ycor()
    assert (posy-ant_posy==24 and posx==ant_posx)
    del player

def test_player_go_down():
    player = Player (walls)
    ant_posx,ant_posy = player.xcor(), player.ycor()
    Player.go_down(player)
    posx , posy = player.xcor(), player.ycor()
    assert (posy-ant_posy==-24 and posx==ant_posx)
    del player


def test_is_collision_enemy():
    player = Player (walls)
    x = player.xcor()
    y = player.ycor()
    enemy = Enemy (walls,ewalls, x, y)
    a = player.xcor() - enemy.xcor()
    b = player.ycor() - enemy.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del player, enemy

def test_is_collision_sickdog():
    player = Player (walls)
    x = player.xcor()
    y = player.ycor()
    enemy = SickDog (walls,ewalls,x, y)
    a = player.xcor() - enemy.xcor()
    b = player.ycor() - enemy.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del player, enemy

def test_is_collision_hueso():
    player = Player (walls)
    x = player.xcor()
    y = player.ycor()
    hueso = Treasure ( x, y)
    a = player.xcor() - hueso.xcor()
    b = player.ycor() - hueso.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del player, hueso

def test_is_collision_trap():
    player = Player (walls)
    x = player.xcor()
    y = player.ycor()
    enemy = Trap ( x, y)
    a = player.xcor() - enemy.xcor()
    b = player.ycor() - enemy.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del player, enemy
    
"""
def test_dies():
    player = Player (walls)
    player.dies()
    x = player.xcor()
    y = player.ycor()
    assert ( x == -4800 and y == -4800)
    del player
"""
def test_walls_player():
    player = Player (walls)
    x = player.xcor()
    y = player.ycor()
    assert ((x, y) not in walls)
    del player


def test_texturas_player_left():
    player= Player (walls)
    player.go_left()
    tex = player.shape()
    assert (tex =="../img/dog.gif")
    del player

def test_texturas_player_up_left():
    player= Player (walls)
    player.go_up()
    player.go_left()
    tex = player.shape()
    assert (tex =="../img/dog.gif")
    del player

def test_texturas_player_up_right():
    player= Player (walls)
    player.go_up()
    player.go_right()
    tex = player.shape()
    assert (tex =="../img/dog_right.gif")
    del player

def test_texturas_player_down_left():
    player= Player (walls)
    player.go_down()
    player.go_left()
    tex = player.shape()
    assert (tex =="../img/dog.gif")
    del player

def test_texturas_player_down_right():
    player= Player (walls)
    player.go_down()
    player.go_right()
    tex = player.shape()
    assert (tex =="../img/dog_right.gif")
    del player

def test_texturas_player_right():
    player= Player (walls)
    player.go_right()
    tex = player.shape()
    assert (tex =="../img/dog_right.gif")
    del player

def test_attack_down_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    player= Player(walls)
    player.go_down()
    if (sickdog.ycor()>player.ycor()):
        sickdog.direction="down"
    assert(sickdog.direction == "down")

def test_attack_up_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    player= Player(walls)
    player.go_up()
    if (sickdog.ycor()<player.ycor()):
        sickdog.direction="up"
    assert(sickdog.direction == "up")

def test_attack_left_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    player= Player(walls)
    player.go_left()
    if (sickdog.xcor()>player.xcor()):
        sickdog.direction="left"
    assert(sickdog.direction == "left")

def test_attack_right_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    player= Player(walls)
    player.go_right()
    if (sickdog.xcor()<player.xcor()):
        sickdog.direction="right"
    assert(sickdog.direction == "right")

def test_attack_down_cazador():
    cazador = Perrero (walls,ewalls,0,0)
    player= Player(walls)
    player.go_down()
    if (cazador.ycor()>player.ycor()):
        cazador.direction="down"
    assert(cazador.direction == "down")

def test_attack_up_cazador():
    cazador = Perrero (walls,ewalls,0,0)
    player= Player(walls)
    player.go_up()
    if (cazador.ycor()<player.ycor()):
        cazador.direction="up"
    assert(cazador.direction == "up")

def test_attack_left_cazador():
    cazador = Perrero (walls,ewalls,0,0)
    player= Player(walls)
    player.go_left()
    if (cazador.xcor()>player.xcor()):
        cazador.direction="left"
    assert(cazador.direction == "left")

def test_attack_right_cazador():
    cazador = Perrero (walls,ewalls,0,0)
    player= Player(walls)
    player.go_right()
    if (cazador.xcor()<player.xcor()):
        cazador.direction="right"
    assert(cazador.direction == "right")

def test_is_close_player_cazador():
    player = Player (walls)
    cazador = Perrero (walls,ewalls,0,0)
    a = player.xcor() - cazador.xcor()
    b = player.ycor() - cazador.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del cazador, player

def test_is_close_player_enemy():
    player = Player (walls)
    enemy = Enemy (walls,ewalls,0,0)
    a = player.xcor() - enemy.xcor()
    b = player.ycor() - enemy.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del enemy, player

def test_is_close_player_sickenemy():
    player = Player (walls)
    enemy = SickDog (walls,ewalls,0,0)
    a = player.xcor() - enemy.xcor()
    b = player.ycor() - enemy.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del enemy, player

def test_is_close_player_hueso():
    player = Player (walls)
    hueso = Treasure(0,0)
    a = player.xcor() - hueso.xcor()
    b = player.ycor() - hueso.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del hueso, player

def test_is_close_player_trampa():
    player = Player (walls)
    trampa = Trap(0,0)
    a = player.xcor() - trampa.xcor()
    b = player.ycor() - trampa.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del trampa, player

def test_is_close_player_flags():
    player = Player (walls)
    flag = Flag(0,0)
    a = player.xcor() - flag.xcor()
    b = player.ycor() - flag.ycor()
    distance = math.sqrt((a**2)+(b**2))
    assert (distance < 75)
    del flag, player











#para realizar la prueba posteriormente se tuvo que colocar un array walls que es requerido por la clase PlayerPerro
level = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP           X          X",
"X               E       X",
"X                      TX",
"XXXXXNNNNNNNNNNNNNNNXXXXX",
"XXXXX               XXXXX",
"XXXXXNNNNOOOOOOOONNNXXXXX",
"X                       X",
"X                       X",
"X                       X",
"X       XXXXXX          X",
"X              E        X",
"X                       X",
"X                       X",
"X      C                X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X T                     X",
"X   XXX           XXX   X",
"X   XXX           XXX   X",
"X   XXX           XXX   X", 
"X                      FX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",]
walls = []
ewalls = []

for y in range(len(level)):
    for x in range(len(level[y])):
        character = level[y][x]
        screen_x = -288 + (x*24)
        screen_y = 288 - (y*24)
        if character == 'X':
            walls.append((screen_x, screen_y))
        if character == 'N':
            ewalls.append((screen_x, screen_y))
        


