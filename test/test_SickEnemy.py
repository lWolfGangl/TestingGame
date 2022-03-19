import math 
import sys 
sys.path.append("../entities")
from SickDogM import SickDog
from TrapMod import Trap
from TreasureMod import Treasure
from PlayerPerro import Player
import unittest
walls = []
ewalls = []
#verifica que el jugador se pueda mover con las teclas
def test_illdog_go_right():
    enemy = SickDog (walls,ewalls,0,0)
    enemy.direction="right"
    enemy.move()
    assert (enemy.xcor()>0)

def test_illdog_go_left():
    enemy = SickDog (walls,ewalls,0,0)
    enemy.direction="left"
    enemy.move()
    assert (enemy.xcor()<0)

def test_illdog_go_up():
    enemy = SickDog (walls,ewalls,0,0)
    enemy.direction="up"
    enemy.move()
    posx , posy = enemy.xcor(), enemy.ycor()
    assert (enemy.ycor()>0)

def test_illdog_go_down():
    enemy = SickDog (walls,ewalls,0,0)
    enemy.direction="down"
    enemy.move()
    assert (enemy.ycor()<0)


def test_illdog_follow():
    player= Player(walls)
    player.go_right()
    player_x, player_y = player.xcor(), player.ycor()

    #ubicar al juegador cerca al perrito con rabia
    enemy = SickDog (walls,ewalls,0,0)
    #se guardan las coordenadas de enemy, y se compara la distancia original con la posterior con distancia euclideana
    pas_x,pas_y=enemy.xcor(),enemy.ycor()
    dist_ant= ((player_x-pas_x)**2+(player_y-pas_y)**2)**0.5 # distancia inicial
    enemy.atackPlayer(player)#cambia direccion
    enemy.move()

    new_x,new_y=enemy.xcor(),enemy.ycor()
    dist_act= ((player_x-new_x)**2+(player_y-new_y)**2)**0.5 # distancia actual
    assert (dist_ant>dist_act)




def test_walls_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    x = sickdog.xcor()
    y = sickdog.ycor()
    assert ((x, y) not in walls)
    del sickdog

def test_ewalls_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    x = sickdog.xcor()
    y = sickdog.ycor()
    assert ((x, y) not in ewalls)
    del sickdog

"""
def test_dies_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.dies()
    x = sickdog.xcor()
    y = sickdog.ycor()
    assert ( x == -4800 and y == -4800)
    del sickdog
"""
def test_is_collision_trap_sickdog():
    sickdog = SickDog (walls,ewalls,0,0)
    x = sickdog.xcor()
    y = sickdog.ycor()
    trap = Trap ( x, y)
    a = sickdog.xcor() - trap.xcor()
    b = sickdog.ycor() - trap.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del sickdog, trap

def test_texturas_sickdog_left():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "left"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/crazydog.gif")
    del sickdog

def test_texturas_sickdog_up_left():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "left"
    sickdog.move()
    sickdog.direction = "up"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/crazydog.gif")
    del sickdog

def test_texturas_sickdog_up_right():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "right"
    sickdog.move()
    sickdog.direction = "up"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/CrazyDogRight.gif")
    del sickdog

def test_texturas_sickdog_down_left():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "left"
    sickdog.move()
    sickdog.direction = "down"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/crazydog.gif")
    del sickdog

def test_texturas_sickdog_down_right():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "right"
    sickdog.move()
    sickdog.direction = "down"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/CrazyDogRight.gif")
    del sickdog

def test_texturas_sickdog_right():
    sickdog = SickDog (walls,ewalls,0,0)
    sickdog.direction = "right"
    sickdog.move()
    tex = sickdog.shape()
    assert (tex =="../img/CrazyDogRight.gif")
    del sickdog
