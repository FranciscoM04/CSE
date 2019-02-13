world_map = {
     'WAR MACHINE': {
         'NAME': "Hallway",
         'DESCRIPTION': "You have now entered the building now choose which "
                        "of the two doors you'l like to take first",
         'PATHS': {
              'EAST': "Gift Shop"
         }
     },
     'GIFT SHOP': {
        'NAME': "Gift Shop",
        'DESCRIPTION': "Now you have entered the gift, now look for the weapon and" 
                       "and on top of it, it has the label on it BoomShot...",
        'Paths': {
              'West': "Ticket Encounter"
         }
    },
     'TICKET ENCOUNTER': {
        'NAME': "Ticket Encounter",
        'DESCRIPTION': "You have made connection with a Giant Bomb so now use your "
                       "weapon to kill it... now look for the Bolo Grenade",
        'Paths': {
              'North': "Bolo Grenade"
        }
     },
     'Security': {
        'NAME': "Security",
        'DESCRIPTION': "",
        'PATHS': ""
     }