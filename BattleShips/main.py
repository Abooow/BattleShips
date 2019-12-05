import re
import os
import battleships
import console_color as color


class State:
    MENU = 0,
    PLACESHIPS = 1,
    YOUPLAYING = 2,
    ENEMYPLAYING = 3,
    YOUWON = 4,
    YOULOST = 5


def pang(attack):
    '''

    param attack(tuple[_,_]):
    returns:
    rtype:
    '''

    attack = attack.replace(' ', '').upper()

    cord = re.match('(?P<letter>[A-J])(?P<num>[0-9)])$', attack) or re.match('(?P<num>[0-9])(?P<letter>[A-J)])$', attack)
    if cord:
        x = int(ord(cord.group('letter')) - 65)
        y = int(cord.group('num'))
        return x, y
    else:
        return None


gamestate = State.MENU

#placing ships state
all_ships_placed = False
shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]


player2 = battleships.Board()
player = battleships.Board()


while True:
    if gamestate == State.MENU:
        color.print_color(r"""                                 _      __      __                        ______        
                                | | /| / /___  / /____ ___   __ _  ___   /_  __/___     
                                | |/ |/ // -_)/ // __// _ \ /  ' \/ -_)   / /  / _ \    
                                |__/|__/ \__//_/ \__/ \___//_/_/_/\__/   /_/   \___/    
                                                         """, color.WHITE)
        color.print_color(r"""     __  ___         __                  ____       __                         _      __            ___               
    /  |/  /___  ___/ /___  ____ ___    / __/__ __ / /_ ____ ___  __ _  ___   | | /| / /___ _ ____ / _/___ _ ____ ___ 
   / /|_/ // _ \/ _  // -_)/ __// _ \  / _/  \ \ // __// __// -_)/  ' \/ -_)  | |/ |/ // _ `// __// _// _ `// __// -_)
  /_/  /_/ \___/\_,_/ \__//_/  /_//_/ /___/ /_\_\ \__//_/   \__//_/_/_/\__/   |__/|__/ \_,_//_/  /_/  \_,_//_/   \__/ 
                                                                                                                    """, color.GREEN)
        print("-" *120)
        print()
        print()
        print()
        print()
        print('1. Start'.center(120))
        print()
        print('2. Quit'.center(120))
        choice = input()
        
        if choice == '1':
            gamestate = State.PLACESHIPS
            os.system('cls')
        elif choice == '2':
            break
        else:
            os.system('cls')

    elif gamestate == State.PLACESHIPS:
        while not all_ships_placed:
            for ship in range(len(shipsAvailable)):
                os.system('cls')
                print('Place your ships onto the battlefield.')
                player.draw()
                counter = 0
                for i in shipsAvailable:
                    counter += 1
                    print(f'{counter}) {i*"O"}')
                print(f'Placing a ship with length {shipsAvailable[0]}.')
                shipLength = shipsAvailable[0]
                validCord = False
                while validCord == False:
                    shipFirstPos = input('Set start coordinate: ')
                    pangCord = pang(shipFirstPos)
                    if pangCord != None: 
                       x = pangCord[0]
                       y = pangCord[1]
                       validCord = True

                while True:
                    shipDirection = input('Set direction(LEFT, RIGHT, UP, DOWN)')
                    if shipDirection.upper() == 'LEFT': 
                        dir = battleships.Ship.LEFT 
                        break
                    elif shipDirection.upper() == 'RIGHT': 
                        dir = battleships.Ship.RIGHT 
                        break
                    elif shipDirection.upper() == 'UP': 
                        dir = battleships.Ship.UP
                        break
                    elif shipDirection.upper() == 'DOWN': 
                        dir = battleships.Ship.DOWN
                        break
                    else: continue

                #Check if its ok to place the boat
                if player.can_place_ship(battleships.Ship((x, y), shipLength, dir)):
                    player.place_ship(battleships.Ship((x, y), shipLength, dir))
                    del shipsAvailable[0]

                if len(shipsAvailable) < 1:
                    all_ships_placed = True
                    os.system('cls')
                    player.draw()
                    gamestate = State.YOUPLAYING
        
    elif gamestate == State.YOULOST:
        print()
        color.print_color(r"""                                     __  __ ____   __  __   __   ____   ____ ______
                                     \ \/ // __ \ / / / /  / /  / __ \ / __//_  __/
                                      \  // /_/ // /_/ /  / /__/ /_/ /_\ \   / /   
                                      /_/ \____/ \____/  /____/\____//___/  /_/    
                                               """, color.RED)
        print()
        print("-" *120)
        print()
        print()
        print()
        print()
        print()
        print()
        print('1. Restart'.center(120))
        print()
        print('2. Main Menu'.center(120))
        choice = input()

        if choice == '1':
            gamestate = State.PLACESHIPS
            os.system('cls')
        elif choice == '2':
            gamestate = State.MENU
            os.system('cls')
        else:
            os.system('cls')

    elif gamestate == State.YOUWON:
        print()
        color.print_color(r"""                                     __  __ ____   __  __   _      __ ____   _  __
                                     \ \/ // __ \ / / / /  | | /| / // __ \ / |/ /
                                      \  // /_/ // /_/ /   | |/ |/ // /_/ //    / 
                                      /_/ \____/ \____/    |__/|__/ \____//_/|_/  
                                              """, color.GREEN)
        print()
        print("-" *120)
        print()
        print()
        print()
        print()
        print()
        print()
        print('1. Restart'.center(120))
        print()
        print('2. Main Menu'.center(120))
        choice = input()

        if choice == '1':
            gamestate = State.PLACESHIPS
            os.system('cls')
        elif choice == '2':
            gamestate = State.MENU
            os.system('cls')
        else:
            os.system('cls')