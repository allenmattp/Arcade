import random

class Cat():
    def __init__(self):
        self.name = ""
        print("A new cat is born!")
        self.color = ""
        self.weight =""

    def meow(self):
        print(self.name, "says Meow")

class Monster():
    def __init__(self, new_name, starting_health):
        self.name = new_name
        print("Oh no a monster!")
        self.health = starting_health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(self.name, "has been slayed!")

def main():
    niles = Cat()
    niles.name = "Niles"
    niles.color = "Gray"
    niles.weight = "11.2 lbs"

    niles.meow()

    dog = Monster("Radley", 100)

    for i in range(random.randrange(1, 10)):
        print("Niles attacks!")
        dog.decrease_health(15)
        
        if dog.health <= 0:
            print(niles.name, "is the victor!")
            break

    if dog.health > 0:
        print(dog.name, "is the victor!")

if __name__ == '__main__':
    main()
