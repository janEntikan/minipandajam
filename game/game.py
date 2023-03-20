from keybindings.device_listener import add_device_listener
from keybindings.device_listener import SinglePlayerAssigner

from game.hell import Hell
from game.clock import Clock
from game.player import Player
from game.enemies import EnemySpawner
from game.background import BackgroundScroller


class Game:
    def __init__(self):
        # Access with base.device_listener.read_context("your context")
        add_device_listener(assigner=SinglePlayerAssigner())
        base.win.set_clear_color((0.3,0.3,0.3,1))
        base.cam.set_z(64)
        base.cam.look_at(0,0,0)

        self.clock = Clock()
        self.hell = Hell()
        self.player = Player()
        self.enemy_spawner = EnemySpawner()
        self.background = BackgroundScroller()


