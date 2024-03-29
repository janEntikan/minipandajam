from panda3d.core import CardMaker
from panda3d.core import Vec3


class Player:

    FPS = 128
    const = 0.03


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
        self.cooldown = 0
        self.cooling = 0.1

    def update(self, task):
        buttons = base.device_listener.read_context("player")
        motion = Vec3(buttons["movement"].x, buttons["movement"].y, 0)
        self.velocity += motion * self.FPS * base.clock.dt
        total_vel = self.velocity * base.clock.dt
        game.clock.update_slowdown(total_vel.length()*3)
        self.root.set_pos(self.root, total_vel)
        self.velocity *= base.clock.dt ** self.const

        self.cooldown += game.clock.dt
        if self.cooldown >= self.cooling:
            self.cooldown -= self.cooling
            game.hell.make_particle(self.root.get_pos(), Vec3(0,10,0))
        return task.cont

