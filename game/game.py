from keybindings.device_listener import add_device_listener
from keybindings.device_listener import SinglePlayerAssigner

from game.hell import Hell
from game.player import Player
from game.enemies import EnemySpawner
from game.background import BackgroundScroller


class Game:
    def __init__(self):
        # Access with base.device_listener.read_context("your context")
        add_device_listener(assigner=SinglePlayerAssigner())

        self.hell = Hell()
        self.player = Player()
        self.enemy_spawner = EnemySpawner()
        self.background = BackgroundScroller()
