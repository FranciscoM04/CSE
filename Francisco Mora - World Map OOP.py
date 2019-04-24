class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = 'description'
        self.characters = []

class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
       """This method searches the current room so see if a room
       exists in that direction.

       :param direction: The direction that you want to move to
       :return: The room object if it exists, or None if it does not
       """
       name_of_room = getattr(self.current_location, direction)
       return globals()[name_of_room]

player = Player[R19A]

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
           next.room = player.find_next_room(command)
           player.move('next_room')
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")

# Option 1 - Define as we go
R19 = Room("Mr. Wiebe's Room", "This is where you are now",)
parking_lot = Room("Parking Lot", None, 'R19A')

'R19A'.north = parking_lot

# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, 'R19A')

player = Player('R19A')

WarMachine = ('WarMachine', None, 'East', "War Machine... watch out this place could be"
                                          "filled with traps.")

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