from random import randint
from panda3d.core import NodePath, CardMaker

class EnemySpawner:
    # Creates enemies at certain intervals.
    pass



class TestEnemySpawner:
    # Creates enemies at certain intervals.
    def __init__(self):
        self.enemy = NodePath("enemy")
        enemy_card = self.enemy.attach_new_node(CardMaker("enemy").generate())
        enemy_card.set_p(-90)
        base.task_mgr.add(self.update)
        self.cooldown = 2

        self.enemies = []

    def update(self, task):
        self.cooldown += game.clock.dt
        if self.cooldown > 2:
            self.cooldown -= 2
            enemy = self.enemy.copy_to(render)
            enemy.set_y(19)
            enemy.set_x(randint(-10,10))
            self.enemies.append(enemy)

        for enemy in self.enemies:
            enemy.set_y(enemy, -5*game.clock.dt)
            if enemy.get_y() <= -20 or game.hell.is_hit(enemy):
                self.enemies.remove(enemy)
                enemy.detach_node()
        return task.cont

