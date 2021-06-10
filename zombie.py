from character import Character

class Zombie(Character):
    def __init__(self):
        super().__init__()
        self.health = float("inf")
        self.power = 1
        
    def attack(self, victim):
        super().attack(victim)
        print("You do %d damage to the goblin." % self.power)

    def is_alive(self):
        return super().is_alive()

    def status(self):
        super().goblin_status()
        #print("The goblin has %d health and %d power." % (self.health, self.power))