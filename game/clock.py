class Clock:
    def __init__(self):
        self.multiplier = 1

    @property
    def dt(self):
        return base.clock.dt*self.multiplier

    def update_slowdown(self, multiplier):
        self.multiplier = multiplier
