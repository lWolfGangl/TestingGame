import math 
import sys 
sys.path.append("../entities")
from PerreroM import Perrero
from TrapMod import Trap
from TreasureMod import Treasure
from PlayerPerro import Player
import unittest
walls = []
ewalls = []
#verifica que el jugador se pueda mover con las teclas


def test_illdog_go_right():
    enemy = Perrero (walls,ewalls,0,0)
    enemy.direction="right"
    enemy.move()
    assert (enemy.xcor()>0)

def test_illdog_go_left():
    enemy = Perrero (walls,ewalls,0,0)
    enemy.direction="left"
    enemy.move()
    assert (enemy.xcor()<0)

def test_illdog_go_up():
    enemy = Perrero (walls,ewalls,0,0)
    enemy.direction="up"
    enemy.move()
    posx , posy = enemy.xcor(), enemy.ycor()
    assert (enemy.ycor()>0)

def test_illdog_go_down():
    enemy = Perrero (walls,ewalls,0,0)
    enemy.direction="down"
    enemy.move()
    assert (enemy.ycor()<0)


def test_illdog_follow():
    player= Player(walls)
    player.go_right()
    player_x, player_y = player.xcor(), player.ycor()

    #ubicar al juegador cerca al perrito con rabia
    enemy = Perrero (walls,ewalls,0,0)
    #se guardan las coordenadas de enemy, y se compara la distancia original con la posterior con distancia euclideana
    pas_x,pas_y=enemy.xcor(),enemy.ycor()
    dist_ant= ((player_x-pas_x)**2+(player_y-pas_y)**2)**0.5 # distancia inicial
    enemy.atackPlayer(player)#cambia direccion
    enemy.move()

    new_x,new_y=enemy.xcor(),enemy.ycor()
    dist_act= ((player_x-new_x)**2+(player_y-new_y)**2)**0.5 # distancia actual
    assert (dist_ant>dist_act)

def test_walls_perrrero():
    perrero = Perrero (walls,ewalls,0,0)
    x = perrero.xcor()
    y = perrero.ycor()
    assert ((x, y) not in walls)
    del perrero

def test_ewalls_perrrero():
    perrero = Perrero (walls,ewalls,0,0)
    x = perrero.xcor()
    y = perrero.ycor()
    assert ((x, y) not in ewalls)
    del perrero

"""
def test_dies_perrrero():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.dies()
    x = perrero.xcor()
    y = perrero.ycor()
    assert ( x == -4800 and y == -4800)
    del perrero
"""
def test_is_collision_trap_perrrero():
    perrero = Perrero (walls,ewalls,0,0)
    x = perrero.xcor()
    y = perrero.ycor()
    trap = Trap ( x, y)
    a = perrero.xcor() - trap.xcor()
    b = perrero.ycor() - trap.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del perrero, trap

def test_texturas_perrrero_left():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "left"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_left.gif")
    del perrero

def test_texturas_perrrero_up_left():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "left"
    perrero.move()
    perrero.direction = "up"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_left.gif")
    del perrero

def test_texturas_perrrero_up_right():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "right"
    perrero.move()
    perrero.direction = "up"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_right.gif")
    del perrero

def test_texturas_perrrero_down_left():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "left"
    perrero.move()
    perrero.direction = "down"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_left.gif")
    del perrero

def test_texturas_perrrero_down_right():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "right"
    perrero.move()
    perrero.direction = "down"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_right.gif")
    del perrero

def test_texturas_perrrero_right():
    perrero = Perrero (walls,ewalls,0,0)
    perrero.direction = "right"
    perrero.move()
    tex = perrero.shape()
    assert (tex =="../img/boss_right.gif")
    del perrero

