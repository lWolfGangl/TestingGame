import sys 
sys.path.append("../entities")
from TreasureMod import Treasure

def test_destroy_hueso():
    hueso = Treasure (1500, 1500)
    hueso.destroy()
    #verificar que se destruye llevando a otra dirección
    assert(hueso.xcor() == 2000 and hueso.ycor() == 2000)
    del hueso

def test_texturas_hueso():
    hueso = Treasure (1500, 1500)
    tex = hueso.shape()
    assert (tex =="../img/bone.gif")
    del hueso

