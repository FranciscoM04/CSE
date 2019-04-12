world_map = {
     'WAR MACHINE': {
         'NAME': "War Machine",
         'DESCRIPTION': "You have now entered the building. Now choose a door"
                        "which one will send you to the Gift Shop while the other"
                        "sends you with an end.",
         'PATHS': {
              'EAST': "HALLWAY"
         }
     },
     'HALLWAY': {
         'NAME': "Hallway1",
         'DESCRIPTION': "When inside the hallway look for any defenses you're now"
                        "looking for an assualt rifle, look quickly before any of the"
                        "Locust come out and find you",
         'PATHS': {
               'SOUTH': "GIFT SHOP"
        }
     },
     'GIFT SHOP': {
        'NAME': "Gift Shop",
        'DESCRIPTION': "Now you have entered the Gift Shop. When entering the Gift Shop"
                       "Locust are coming your way... SHOOT!!! Get to the hallway as fast"
                       "as you can before you get killed",
        'PATHS': {
              'WEST': "HALLWAY2"
         }
     },
     'HALLWAY2': {
        'NAME': "Hallway2",
        'DESCRIPTION': "When you have entered the second hallway, look around for the first"
                       "switch, it's the switch that will help threw the map. Follow the lights"
                       "and watch out anything can pop out at any moment.",

        'PATHS': {
            'North': "TICKET ENCOUNTER"
        }
     },
     'TICKET ENCOUNTER': {
        'NAME': "Ticket Encounter",
        'DESCRIPTION': "You have made connection with a Giant Bomb. Look for Bolo"
                       "Grenades. Throw them right under the Giant Bomb. Take cover"
                       "it's coming closer towards you.",
        'Paths': {
              'North': "HALLWAY3"
        }
     },
     'HALLWAY3':{
         'NAME': "Hallway3",
         'DESCRIPTION': "Now, you have entered the third hallway. Look for any supplies"
                        "such as aid kit and any kind of weapons for use to defend"
                        "yourself. Hurry move into the Security room their are more ammo"
                        "to defend yourself and kill the Bowing Locust!",

         'PATHS': {
             'East': "SECURITY"
         }     
     },
     'SECURITY': {
        'NAME': "Security",
        'DESCRIPTION': "You are now in the Security Room you are now safe from all of the"
                       "Locust. Okay now the second switch is in here. You just got to look around"
                       "because I don't know where it's located.",
        'PATHS': {
            'South': "HALLWAY4"
        }
     },
     'HALLWAY4': {
         'NAME': "Hallway4",
         'DESCRIPTION': "Your now in hallway4 four their is none thing much else to do all"
                        "you'll have to do is find the key to open the door, now look around",
         'PATHS': {
             'East': "PLATE FORM GATE"
         }
     },
     'PLATE FORM GATE': {
         'NAME': "Plate Form Gate",
         'DESCRIPTION': "This is the Plate Form Gate. Now look for the switch. They're"
                        "going to be three switches located in the Plate Form Gate room.",
         'PATHS': {
            'West': "Plate Form Gate2"
         }
     },
     'Plate Form Gate2': {
         'NAME': "Plate Form Gate2",
         'DESCRIPTION': "",
         'PATHS': {
            'North': "NORTH EXIT"
         }
     },
     'NORTH EXIT': {
         'NAME': "",
         'DESCRIPTION': "",
         'PATHS': {
            'South': "SOUTH EXIT"
         }
     },

}


# Controller
playing = True
current_node = world_map['WAR MACHINE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")