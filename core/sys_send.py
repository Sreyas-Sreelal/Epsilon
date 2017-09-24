# ~ src/sys_send.py

"""

This module is responsible for sending colorful text messages to user.

"""

from colorama import init
init( autoreset = True ); # clean the terminal after splashing colors on them
from colorama import Fore, Back, Style


def print_title( ):
    print( "\n\n\t\t\t\t" + Fore.YELLOW + "Epsilon " + Fore.MAGENTA + " Python Version " + Fore.GREEN + "By" + Fore.RED + " SREYAS" );
    return ""

def print_blue( str ):
    print( Style.BRIGHT + Fore.BLUE + str );
    return ""

def print_magenta( str ):
    print( Style.BRIGHT + Fore.MAGENTA + str );
    return ""

def print_red( str ):
    print( Style.BRIGHT + Fore.RED + str );  
    return ""

def print_white( str ):
    print( Style.BRIGHT + Fore.WHITE + str );
    return ""

def print_green( str ):
    print( Style.BRIGHT + Fore.GREEN + str );
    return ""

def print_yellow( str ):
    print(  Style.BRIGHT + Fore.YELLOW + str  );
    return ""

def print_cyan( str ):
    print(  Style.BRIGHT + Fore.CYAN + str  );
    return ""

def success( str ):
    print( Style.BRIGHT + Fore.YELLOW + "\n[***]" + Fore.GREEN + str );
    return ""

def warning( str ):
    print( Style.BRIGHT + Fore.RED + "[WARNING!]" + Style.NORMAL + str );
    return ""

def error ( str ):
    print( Style.BRIGHT + Fore.RED + "[Error] " + str );
    return ""

def ask( str ):
    print( Style.BRIGHT + Fore.WHITE + "Input " + str );
    return ""

def prompt( str ):
    print( Style.BRIGHT + Fore.WHITE + "Press " + str );
    return ""

def code( str ):
    print( Style.BRIGHT + Back.BLACK + Fore.GREEN + str );
    return ""

# a little class that needed to be expanded for future purposes

class term_style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_bold( str , color = Fore.WHITE ):
    print( term_style.BOLD + str );
    return ""

def print_underlined( str , color = Fore.WHITE ):
    print( term_style.UNDERLINE + str );
    return ""







