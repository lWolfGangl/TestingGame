
import unittest

def test_check_pared_level1():
    pared = False
    for line in level:
        for character in line:
            if character == "X":
                pared = True
    assert (pared)

def test_check_pared_level2():
    pared = False
    for line in level_2:
        for character in line:
            if character == "X":
                pared = True
    assert (pared)

def test_check_pared_level3():
    pared = False
    for line in level_3:
        for character in line:
            if character == "X":
                pared = True
    assert (pared)

def test_check_pared_level4():
    pared = False
    for line in level_4:
        for character in line:
            if character == "X":
                pared = True
    assert (pared)


def test_check_enemy_level1():
    enemigo = False
    for line in level:
        for character in line:
            if character == "E":
                enemigo = True
    assert (enemigo)

def test_check_enemy_level2():
    enemigo = False
    for line in level_2:
        for character in line:
            if character == "E":
                enemigo = True
    assert (enemigo)

def test_check_enemy_level3():
    enemigo = False
    for line in level_3:
        for character in line:
            if character == "E":
                enemigo = True
    assert (enemigo)

def test_check_enemy_level4():
    enemigo = False
    for line in level_4:
        for character in line:
            if character == "E":
                enemigo = True
    assert (enemigo)

def test_check_player_level1():
    perrito = False
    for line in level:
        for character in line:
            if character == "P":
                perrito = True
    assert (perrito)

def test_check_player_level2():
    perrito = False
    for line in level_2:
        for character in line:
            if character == "P":
                perrito = True
    assert (perrito)

def test_check_player_level3():
    perrito = False
    for line in level_3:
        for character in line:
            if character == "P":
                perrito = True
    assert (perrito)

def test_check_player_level4():
    perrito = False
    for line in level_4:
        for character in line:
            if character == "P":
                perrito = True
    assert (perrito)
    
def test_check_trampas_level1():
    trampas = False
    for line in level:
        for character in line:
            if character == "O":
                trampas = True
    assert (trampas)

def test_check_trampas_level2():
    trampas = False
    for line in level_2:
        for character in line:
            if character == "O":
                trampas = True
    assert (trampas)

def test_check_trampas_level3():
    trampas = False
    for line in level_3:
        for character in line:
            if character == "O":
                trampas = True
    assert (trampas)

def test_check_trampas_level4():
    trampas = False
    for line in level_4:
        for character in line:
            if character == "O":
                trampas = True
    assert (trampas)

def test_check_ewalls_level1():
    ewalls = False
    for line in level:
        for character in line:
            if character == "N":
                ewalls = True
    assert (ewalls)

def test_check_ewalls_level2():
    ewalls = False
    for line in level_2:
        for character in line:
            if character == "N":
                ewalls = True
    assert (ewalls)

def test_check_ewalls_level3():
    ewalls = False
    for line in level_3:
        for character in line:
            if character == "N":
                ewalls = True
    assert (ewalls)

def test_check_ewalls_level4():
    ewalls = False
    for line in level_4:
        for character in line:
            if character == "N":
                ewalls = True
    assert (ewalls)

def test_check_crazydog_level1():
    rabia = False
    for line in level:
        for character in line:
            if character == "C":
                rabia = True
    assert (rabia)

def test_check_crazydog_level2():
    rabia = False
    for line in level_2:
        for character in line:
            if character == "C":
                rabia = True
    assert (rabia)

def test_check_crazydog_level3():
    rabia = False
    for line in level_3:
        for character in line:
            if character == "C":
                rabia = True
    assert (rabia)

def test_check_crazydog_level4():
    rabia = False
    for line in level_4:
        for character in line:
            if character == "C":
                rabia = True
    assert (rabia)

def test_check_tesoro_level1():
    hueso = False
    for line in level:
        for character in line:
            if character == "T":
                hueso = True
    assert (hueso)

def test_check_tesoro_level2():
    hueso = False
    for line in level_2:
        for character in line:
            if character == "T":
                hueso = True
    assert (hueso)

def test_check_tesoro_level3():
    hueso = False
    for line in level_3:
        for character in line:
            if character == "T":
                hueso = True
    assert (hueso)

def test_check_tesoro_level4():
    hueso = False
    for line in level_4:
        for character in line:
            if character == "T":
                hueso = True
    assert (hueso)

def test_check_player1_level1():
    con = 0
    for line in level:
        for character in line:
            if character == "P":
                con = con +1
    assert (con == 1)

def test_check_player1_level2():
    con = 0
    for line in level_2:
        for character in line:
            if character == "P":
                con = con +1
    assert (con == 1)

def test_check_player1_level3():
    con = 0
    for line in level_3:
        for character in line:
            if character == "P":
                con = con +1
    assert (con == 1)

def test_check_player1_level4():
    con = 0
    for line in level_4:
        for character in line:
            if character == "P":
                con = con +1
    assert (con == 1)

def test_check_flags_level1():
    flag = False
    for line in level_2:
        for character in line:
            if character == "F":
                flag = True
    assert (flag)

def test_check_flags_level2():
    flag = False
    for line in level_2:
        for character in line:
            if character == "F":
                flag = True
    assert (flag)

def test_check_flags_level3():
    flag = False
    for line in level_3:
        for character in line:
            if character == "F":
                flag = True
    assert (flag)

def test_check_flags_level4():
    flag = False
    for line in level_4:
        for character in line:
            if character != "F":
                flag = True
    assert (flag)

def test_check_ninio_level1():
    ninio = False
    for line in level:
        for character in line:
            if character != "B":
                ninio = True
    assert (ninio)

def test_check_ninio_level2():
    ninio = False
    for line in level_2:
        for character in line:
            if character != "B":
                ninio = True
    assert (ninio)

def test_check_ninio_level3():
    ninio = False
    for line in level_3:
        for character in line:
            if character != "B":
                ninio = True
    assert (ninio)

def test_check_ninio_level4():
    ninio = False
    for line in level_4:
        for character in line:
            if character == "B":
                ninio = True
    assert (ninio)

def test_check_cazador_level1():
    cazador = False
    for line in level:
        for character in line:
            if character != "S":
                cazador = True
    assert (cazador)

def test_check_cazador_level2():
    cazador = False
    for line in level_2:
        for character in line:
            if character != "S":
                cazador = True
    assert (cazador)

def test_check_cazador_level3():
    cazador = False
    for line in level_3:
        for character in line:
            if character == "S":
                cazador = True
    assert (cazador)

def test_check_cazador_level4():
    cazador = False
    for line in level_4:
        for character in line:
            if character == "S":
                cazador = True
    assert (cazador)

def test_check_cazador1_level3():
    con = 0
    for line in level_3:
        for character in line:
            if character == "S":
                con = con +1
    assert (con == 1)


level = [
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
