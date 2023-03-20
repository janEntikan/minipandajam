from panda3d.core import CardMaker
from panda3d.core import Vec3


class Player:
    def __init__(self):
        self.root = render.attach_new_node("player")
        card = self.root.attach_new_node(CardMaker("player").generate())
        card.set_p(-90)
        texture = base.loader.load_texture("assets/images/player.png")
        texture.set_minfilter(0);texture.set_magfilter(0)
        card.set_texture(texture)
        card.set_transparency(True)
        self.velocity = Vec3()
        base.task_mgr.add(self.update)

    def update(self, task):
        buttons = base.device_listener.read_context("player")
        motion = Vec3(buttons["movement"].x, buttons["movement"].y, 0)
        self.velocity += motion*128*base.clock.dt
        self.root.set_pos(self.root, self.velocity*base.clock.dt)
        self.velocity *= base.clock.dt**0.04
        game.clock.update_slowdown(motion.length())
        return task.cont
