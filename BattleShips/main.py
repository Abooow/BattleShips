import re
import os
import battleships
import console_color as color
import pygame
from pygame.locals import *
from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize

class State:
    MENU = 0,
    PLACESHIPS = 1,
    YOUPLAYING = 2,
    ENEMYPLAYING = 3,
    YOUWON = 4,
    YOULOST = 5



pygame.init()
x = 1000
y = 655

screen = pygame.display.set_mode((x,y),RESIZABLE)



pygame.display.set_caption('Sink a skipp')
background_colour = (255,255,255)
screen.fill(background_colour)

clip = VideoFileClip(r'C:\Users\stefa\Pictures\puff.mp4', resize((x,y)))
clip.preview()

start = pygame.image.load(r'C:\Users\stefa\Downloads\Menu_test4.png')
start = pygame.transform.scale(start, (1000, 800))
screen.blit(start, (0, -145))


done = False
gamestate = State.MENU
while not done:
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN and 300 <= mx <= 700 and 244 <= my <= 312:
            print('jippie')
            gamestate = State.PLACESHIPS
    pygame.display.flip()
    if gamestate == State.PLACESHIPS:
        background_colour = (0, 0, 0)
        screen.fill(background_colour)
        start = pygame.image.load(r'C:\Users\stefa\Downloads\water_texture.png')
        start = pygame.transform.scale(start, (500, 800))
        screen.blit(start, (250, 0))
        grid = pygame.image.load(r'C:\Users\stefa\Downloads\a1.png')
        grid = pygame.transform.scale(grid, (640, 350))
        screen.blit(grid, (190, -30))
        grid_2 = pygame.image.load(r'C:\Users\stefa\Downloads\a1.png')
        grid_2 = pygame.transform.scale(grid_2, (640, 350))
        screen.blit(grid, (190, 330))
        screen.fill(background_colour)
        skepp = pygame.image.load(r'C:\Users\stefa\Downloads\shipz\images\ship_large_body.png')
        skepp = pygame.transform.scale(skepp, (x, y))
        skepp = pygame.transform.rotate(skepp, 270)
        screen.blit(skepp, (10, 50))
        pygame.display.update()






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




#placing ships state
all_ships_placed = False
shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]


player = battleships.Board()
player2 = battleships.AI()


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
                    player2.place_ship()
                    gamestate = State.YOUPLAYING

    elif gamestate == State.YOUPLAYING:
        print('AI'.center(22))
        player2.board.draw_anonymously()
        print()
        print('You'.center(22))
        player.draw()

        coordinate = pang(input('Select a coordinate to shoot at: '))
        if coordinate != None:
            shot = player2.board.shoot(coordinate)
            if shot[0]:
                if shot[1] != None:
                    print('Hit!')
                    if shot[1].health <= 0:
                        print('You sunk a ship!')
                        if len(player2.board.ships) == 0:
                            print('You sunk all the ships!!!')
                            input()
                            gamestate = State.YOUWON
                            os.system('cls')
                            continue
                else:
                    print('Miss!')
                input()
                gamestate = State.ENEMYPLAYING
                os.system('cls')
            else:
                print("can't shoot at the same place twice!")
                input()
                os.system('cls')
        else:
            os.system('cls')
            continue
    elif gamestate == State.ENEMYPLAYING:
        print('AI'.center(22))
        player2.board.draw_anonymously()
        print()
        print('You'.center(22))
        player.draw()

        shot = player2.shoot(player)
        if shot[1] != None:
            print('You got hit!')
            input()
            os.system('cls')
        else:
            print('AI missed!')
            input()
            os.system('cls')

        if len(player.ships) == 0:
            gamestate = State.YOULOST
        else:
            gamestate = State.YOUPLAYING

    elif gamestate == State.YOULOST:
        print()
        color.print_color(r"""                                    __  __ ____   __  __   __   ____   ____ ______
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

        all_ships_placed = False
        shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]
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
        color.print_color(r"""                                      __  __ ____   __  __   _      __ ____   _  __
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

        shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]
        gamestate = State.PLACESHIPS
        if choice == '1':
            all_ships_placed = False
            os.system('cls')
        elif choice == '2':
            gamestate = State.MENU
            os.system('cls')
        else:
            os.system('cls')
