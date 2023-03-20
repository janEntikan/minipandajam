from panda3d.core import NodePath, CardMaker

# makes bullets and checks for collisions
class Hell:
    def __init__(self):
        self.bullet_kinds = {}
        self.bullets_on_screen = []

        self.bullet = NodePath("bullet")
        bullet_graphic = self.bullet.attach_new_node(CardMaker("bullet").generate())
        bullet_graphic.set_p(-90)
        bullet_graphic.set_scale((0.1,0.2,0.1))
        bullet_graphic.set_pos(0.4, 0.5, 0)
        base.task_mgr.add(self.update)

    def update(self, task):
        for bullet in self.bullets_on_screen:
            bullet.set_y(bullet, 20*game.clock.dt)
            if abs(bullet.get_y()) > 20:
                self.bullets_on_screen.remove(bullet)
                bullet.detach_node()
        return task.cont

    def spawn_bullet(self, pos, kind=None, mask=0):
        bullet = self.bullet.copy_to(render)
        bullet.set_pos(pos)
        self.bullets_on_screen.append(bullet)




