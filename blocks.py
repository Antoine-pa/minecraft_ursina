import ursina
from base import Textures
ursina.window.borderles = False


class InitGame(Textures):
    def __init__(self):
        Textures.__init__(self)

    def build_init(self, width = 10, height = 7, length = 10):
        for x in range(width):
            for _y in range(1, height+1):
                for z in range(length):
                    y = -_y-1
                    if _y == 1:
                        Block((x,y,z))
                    else:
                        Block((x,y,z), texture=self.stone_texture)



class Block(Textures, ursina.Button):
    def __init__(self, position = (0,0,0), texture = None):
        Textures.__init__(self)
        if texture is None:
            texture = self.grass_texture
        ursina.Button.__init__(self,
			parent = ursina.scene,
			position = position,
			model = "assets/block",
			origin_y = 0,
			texture = texture,
			color = ursina.color.color(0,0,ursina.random.uniform(0.9,1)),
			scale = 0.5)
        #self.max_resistance = 1

    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                file = open("data/data.txt", "r")
                block_pick = file.readline()[0]
                file.close()
                Block(position = self.position + ursina.mouse.normal, texture = self.textures_blocks.get(block_pick))

            if key == "right mouse down":
                #punch_sound.play()
                ursina.destroy(self)