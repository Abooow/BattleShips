import os

os.system('color')

RESET = '\u001b[0m'
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
LIGHTBLACK = '\u001b[30;1m'
LIGHTRED = '\u001b[31;1m'
LIGHTGREEN = '\u001b[32;1m'
LIGHTYELLOW = '\u001b[33;1m'
LIGHTBLUE = '\u001b[34;1m'
LIGHTMAGENTA = '\u001b[35;1m'
LIGHTCYAN = '\u001b[36;1m'
LIGHTWHITE = '\u001b[37;1m'

def print_color(string, color, end='\n'):
    print(f'{color}{string}{RESET}', end=end)