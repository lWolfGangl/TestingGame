import sys 
sys.path.append("../entities")
from PlayerPerro import Player
from Enemies import Enemy
from SickDogM import SickDog
from TrapMod import Trap
from TreasureMod import Treasure
import unittest
import math

def test_destroy_trap():
    trampa = Trap (1500, 1500)
    trampa.destroy()
    #verificar que se destruye llevando a otra dirección
    assert(trampa.xcor() == 2000 and trampa.ycor() == 2000)

def test_texturas_trampas():
    trampa = Trap (1500, 1500)
    tex = trampa.shape()
    assert (tex =="../img/hole.gif")
