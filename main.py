import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from base import Textures
from blocks import Block, InitGame
from hand import Hand
from sky import _Sky
from menu import Menu

file = open("data/data.txt", "w")
file.write("1")
file.close()

length = 20 #longeur (z)
width = 20  #largeur (x)
height = 7  #hauteur (y)


ursina.window.borderles = False
app = ursina.Ursina()

list_key = ["1", "2", "3", "4", "left mouse", "right mouse"]
list_key_blocks = ["1", "2", "3", "4"]
list_key_mouse = ["left mouse", "right mouse"]

class Data:
    def __init__(self, menu):
        self.menu = menu

data = Data("open")
textures = Textures()
player = FirstPersonController(origin_t = 1, speed = 8)
hand = Hand()
sky = _Sky()
menu = Menu()
block = Block()
init = InitGame()
if data.menu == "open":
    menu.update_menu()

def update():
    for key in list_key:
        if key in ursina.held_keys and ursina.held_keys[key] == 1:
            if key in list_key_blocks:
                file = open("data/data.txt", "w")
                file.write(key)
                file.close()

    if ursina.held_keys['left mouse'] or ursina.held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

init.build_init()

app.run()