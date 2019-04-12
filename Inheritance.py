class Vehicle(object):
    def __init__(self, name):
        self.name  = name

class Car(Vehicle)
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_satus = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        self.fuel -= 1
        print("The car turns left")

    def turns_off(self):
        self.engine_satus = False
        print("You turn off the car")

class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)

class KeylessCar(Car):
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name, milage)

    def start_engine(self):
        self.engine_satus = True
        print("You push the button and the car turns on.")

wiebe_car = KeylessCar("Tesla", 125)

jacob_car = Impala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_off()

class Item(object):
    def __init__(self, name):
        self.name = name

class Weapon(Item)
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt

class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage
            print("No damage is done because of some AMAZING armor.")
        else:
           self.health -= damage - self.armor.armor_amt
           print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

# Items

sword = Weapon("sword", 10)
canoe = Weapon("Canoe", 42)
wiebe_armor = Armor("Armor of the gods", 100000000000000000000000)

# Characters
orc = Character("Orcl", 100, sword, Armor("Generic Armor", 2))
orc2 = Character("Wiebe", 10000, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)