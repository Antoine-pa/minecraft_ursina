import ursina
from base import Textures
ursina.window.borderles = False
class Hand(Textures, ursina.Entity):
    def __init__(self):
        Textures.__init__(self)
        ursina.Entity.__init__(self,
            parent = ursina.camera.ui,
            model = "assets/arm",
            texture = self.arm_texture,
            scale = 0.2,
            rotation = ursina.Vec3(150,-10,0),
            position = ursina.Vec2(0.4,-0.6))

    def active(self):
        self.position = ursina.Vec2(0.3,-0.5)

    def passive(self):
        self.position = ursina.Vec2(0.4,-0.6)