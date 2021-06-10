from character import Character


from character import Character

class Goblin(Character):
    def __init__(self):
        super().__init__()
        self.health -= 4
        self.power -= 3
        # self.health = 6
        # self.power = 2
        
    def attack(self, victim):
        super().attack(victim)
        print("Goblin does %d damage to you." % self.power)

    def is_alive(self):
        return super().is_alive()

    def status(self):
        super().goblin_status()
        #print("The goblin has %d health and %d power." % (self.health, self.power))