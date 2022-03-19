import sys 
sys.path.append("../entities")
from PlayerPerro import Player
from Enemies import Enemy
from SickDogM import SickDog
from TrapMod import Trap
from TreasureMod import Treasure
import unittest
import math


walls = []
ewalls = []
#verifica que el jugador se pueda mover con las teclas
def test_enemy_go_right():
    enemy = Enemy (walls,ewalls,0,0)
    enemy.direction="right"
    enemy.move()
    assert (enemy.xcor()>0)
    del enemy

def test_enemy_go_left():
    enemy = Enemy (walls,ewalls,0,0)
    enemy.direction="left"
    enemy.move()
    assert (enemy.xcor()<0)
    del enemy

def test_enemy_go_up():
    enemy = Enemy (walls,ewalls,0,0)
    enemy.direction="up"
    enemy.move()
    posx , posy = enemy.xcor(), enemy.ycor()
    assert (enemy.ycor()>0)
    del enemy

def test_enemy_go_down():
    enemy = Enemy (walls,ewalls,0,0)
    enemy.direction="down"
    enemy.move()
    assert (enemy.ycor()<0)
    del enemy

def test_walls_enemy():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    x = enemy.xcor()
    y = enemy.ycor()
    assert ((x, y) not in walls)
    del enemy

def test_ewalls_enemy():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    x = enemy.xcor()
    y = enemy.ycor()
    assert ((x, y) not in ewalls)
    del enemy
    
"""
def test_dies_enemy():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.dies()
    x = enemy.xcor()
    y = enemy.ycor()
    assert ( x == -4800 and y == -4800)
    del enemy
"""

def test_is_collision_trap_enemy():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    x = enemy.xcor()
    y = enemy.ycor()
    trap = Trap ( x, y)
    a = enemy.xcor() - trap.xcor()
    b = enemy.ycor() - trap.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    assert (distance < 5)
    del enemy, trap


def test_texturas_enemy_left():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "left"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catleft.gif")
    del enemy

def test_texturas_enemy_up_left():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "left"
    enemy.move()
    enemy.direction = "up"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catleft.gif")
    del enemy

def test_texturas_enemy_up_right():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "right"
    enemy.move()
    enemy.direction = "up"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catright.gif")
    del enemy

def test_texturas_enemy_down_left():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "left"
    enemy.move()
    enemy.direction = "down"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catleft.gif")
    del enemy

def test_texturas_enemy_down_right():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "right"
    enemy.move()
    enemy.direction = "down"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catright.gif")
    del enemy

def test_texturas_enemy_right():
    enemy = Enemy (walls,ewalls, 1500, 1500)
    enemy.direction = "right"
    enemy.move()
    tex = enemy.shape()
    assert (tex =="../img/catright.gif")
    del enemy
