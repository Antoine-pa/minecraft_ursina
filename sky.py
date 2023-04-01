import ursina
from base import Textures
ursina.window.borderles = False
class _Sky(Textures, ursina.Entity):
    def __init__(self):
        Textures.__init__(self)
        ursina.Entity.__init__(self,
            parent = ursina.scene,
            model = "sphere",
            texture = self.sky_texture,
            scale = 150,
            double_sided = True)
