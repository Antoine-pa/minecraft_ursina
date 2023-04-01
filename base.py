import ursina
ursina.window.borderles = False
class Textures:
    def __init__(self):
        self.grass_texture = ursina.load_texture('assets/grass_block.png')
        self.stone_texture = ursina.load_texture('assets/stone_block.png')
        self.brick_texture = ursina.load_texture('assets/brick_block.png')
        self.dirt_texture = ursina.load_texture('assets/dirt_block.png')
        self.sky_texture = ursina.load_texture('assets/skybox.png')
        self.arm_texture = ursina.load_texture('assets/arm_texture.png')
        self.textures_blocks = {
            "1" : (self.grass_texture),
            "2" : (self.stone_texture),
            "3" : (self.dirt_texture),
            "4" : (self.brick_texture)}