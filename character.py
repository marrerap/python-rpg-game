
class Character:
    def __init__(self):
        
        self.health = 10
        self.power = 5

    def attack(self, victim):
        victim.health -= self.power

    def is_alive(self):
        if self.health > 0:
            return True

    def hero_status(self):
        print("The hero has %d health and %d power." % (self.health, self.power))

    def goblin_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))