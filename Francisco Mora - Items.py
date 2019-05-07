WarMachine = ('WarMachine', None, 'East', "War Machine... watch out this place could be filled with traps. Now,"
                                          "once we have entered we are looking for")

Hallway1 = ('Hallway1', None, None, 'South', "")

GiftShop = ('GiftShop', None, None, None, 'West', "")

Hallway2 = ('Hallway2', None, 'North')

TicketEncounter = ('TicketEncounter', None, None, None, 'North', "")

Hallway3 = ('Hallway3', None, 'East', "")

Security = ('Security', None, None, 'South', "")

Hallway4 = ('Hallway4', None, None, None, 'East', "")

PlateFormGate = ('PlateFormGate', None, 'West', "")

PlateFormGate2 = ('PlateFormGate2', None, None, 'North', "")

NorthExit = ('NorthExit', None, None, None, 'North', "")

SouthExit = ('SouthExit', None, 'South', "")


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
        super(Sniper_rifle, self).__init__("Sniper Rifle", 150, 200)

class Boltok_Pistol(Weapons):
    def __init__(self):
        super(Boltok_Pistol, self).__init__("Boltok Pistol", 80, 50)

class Assualt_rifle(Weapons):
    def __init__(self):
        super(Assualt_rifle, self).__init__("Assualt Rifle", 100, 80)

class Grenade_Launcher(Weapons):
    def __init__(self):
        super(Grenade_Launcher, self).__init__("Grenade Launcher", 120, 150)
        self.grenades = 15

class Characters(object):
    def __init__(self, name):
        self.name = name

class Enemies(Item):
    def __init__(self):