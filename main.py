import sys
import builtins
from direct.showbase.ShowBase import ShowBase
from game.game import Game


base = ShowBase()
base.accept("escape", sys.exit)
builtins.game = base.game = Game()
base.run()
