from panda3d.core import NodePath, CardMaker
from panda3d.core import Vec3

# importing player class as we will be using some of its functionalities
from player import Player

# makes bullets and checks for collisions
class Hell:
    def __init__(self):
        self.bullet_kinds = {}
        self.bullets_on_screen = []
        self.velocity = 0 # speed of bullet

        self.acc_factor = 0 # For taking acceleration of bullet

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

    def is_hit(self, who):
        # Function for checking did bullet hit the target
        return False
    
    def bullet_acc(self, acc):
        # accelerates or decelerates bullet based on the value of acc
        self.velocity += acc * base.clock.dt
        return

    def bullet_physics(self):
        # bullet becomes slower if player slows down
        
        """How to detect change in velocity of player?"""
        old_vel = Player.velocity # Get player's  original velocity
        Player.update()
        new_vel = Player.velocity # Get player's velocity after updating

        self.acc_factor = (new_vel - old_vel)/ base.clock.dt
        self.bullet_acc(acc=self.acc_factor)
        return
    
