import sys 
sys.path.append("../entities")
from flags import Flag

def test_destroy_flag():
    flag = Flag (1500, 1500)
    flag.destroy()
    #verificar que se destruye llevando a otra dirección
    assert(flag.xcor() == 2000 and flag.ycor() == 2000)
    del flag

def test_texturas_flag():
    flag = Flag (1500, 1500)
    tex = flag.shape()
    assert (tex =="../img/flag.gif")
    del flag