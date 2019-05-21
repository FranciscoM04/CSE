
class Item(object):
    def __init__(self, name):
        self.name = name

class Weapons(Item):
    def __init__(self, name, range, damage):
        super(Weapons, self).__init__(name)
        self.range = range
        self.damage = damage
                                                
class Sniper_rifle(Weapons):
    def __init__(self):
        super(Sniper_rifle, self).__init__("Sniper Rifle", 100, 150)

class Boltok_Pistol(Weapons):
    def __init__(self):
        super(Boltok_Pistol, self).__init__("Boltok Pistol", 80, 50)

class Assualt_rifle(Weapons):
    def __init__(self):
        super(Assualt_rifle, self).__init__("Assualt Rifle", 100, 80)

class Grenade_Launcher(Weapons):
    def __init__(self):
        super(Grenade_Launcher, self).__init__("Grenade Launcher", 120, 150)
        self.grenades = 10

class Characters(object):
    def __init__(self, name):
        self.name = name

class Enemies(Item):
    def __init__(self, name):
        self.name = name

class Characters(Enemies):
    def __init__(self, name, health, weapon, range, damage):
         super(Weapons, self)._init_(name)
         self.health = health
         self.weapon = weapon
         self.range = range
         self.damage = damage

class LocustRager(Enemies):
    def __init__(self):
        super(LocustRager, self).__init__("LocustRager", 100, "None")

class Brumak(Enemies):
    def __init__(self):
        super(Brumak, self).__init__("Brumak", 200, "LivingTanks")

class ArmouredKantus(Enemies):
    def __init__(self):
        super(ArmouredKantus, self).__init__("ArmouredKantus", 150, "TwinGorgons")

class Serapede(Enemies):
    def __init__(self):
        super(Serapede, self).__init__("Serapede", 100, "AcidicPoison")

class Wretch(Enemies):
    def __init__(self):
        super(Wretch, self).__init__("Wretch", 100, "")