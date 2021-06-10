"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
from hero import Hero
from goblin import Goblin

def main():
    hero_1 = Hero()
    goblin_1 = Goblin()
    ## hero_health = 10
    ## hero_power = 5
    ## goblin_health = 6
    ## goblin_power = 2

    while goblin_1.is_alive() and hero_1.is_alive():
        ## goblin_1.health > 0 and hero_1.health > 0:
        hero_1.status()
        ## print("You have %d health and %d power." % (hero_1.health, hero_1.power))
        goblin_1.status()
        ##print("The goblin has %d health and %d power." % (goblin_1.health, goblin_1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero_1.attack(goblin_1)            
            ## goblin_1.health -= hero_1.power
            ## print("You do %d damage to the goblin." % hero_1.power)
            if not goblin_1.is_alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_1.is_alive():
            # Goblin attacks hero
            goblin_1.attack(hero_1)
            
            ## hero_1.health -= goblin_1.power
            ## print("The goblin does %d damage to you." % goblin_1.power)
            if not hero_1.is_alive():
                print("You are dead.")

main()