from random import randint
from panda3d.core import NodePath, CardMaker

from .tools import sheet_card


class Enemy:
    def __init__(self, pos=(0,0,0), image="enemy"):
        self.hp =  1
        self.root = sheet_card("enemy").copy_to(render)
        self.root.set_pos(pos)
        self.lifetime = 0
        base.task_mgr.add(self.update)

    def movement(self):
        pass

    def update(self, task):
        self.lifetime += game.clock.dt
        self.root.set_y(self.root, -5*game.clock.dt)
        if self.root.get_y() <= -20 or game.hell.is_colliding(self.root):
            self.root.detach_node()
            return task.done
        self.movement()
        return task.cont


class EnemySpawner:
    def __init__(self, level=0):
        base.task_mgr.add(self.update)
        self.cooling = 2
        self.cooldown = self.cooling
        self.enemies = []

    def update(self, task):
        self.cooldown += game.clock.dt
        if self.cooldown > self.cooling:
            self.cooldown -= self.cooling
            Enemy(pos=(randint(-20,20), 19, 0))
        return task.cont

