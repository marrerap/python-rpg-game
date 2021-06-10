from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        
       #

    def attack(self, victim):
        super().attack(victim)
        print("You do %d damage to the goblin." % self.power)

    def is_alive(self):
        return super().is_alive()

    def status(self):
        super().hero_status()

        #print("You have %d health and %d power." % (self.health, self.power))
