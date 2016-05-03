from __future__ import print_function
from os import system
from riddles import *
import sys, termios

filenames = {
            'and':'and.txt',
            'or':'or.txt',
            'not':'not.txt',
            'impl':'impl.txt'
            }

#####################
#                   #
#   Function        #
#   definitions     #
#                   #
#####################

def init():
    #
    # Argument parsing
    #
    control_string = ""
    for arg in sys.argv[1:]:
        if control_string != "":
            filenames[control_string] = arg
            control_string = ""
        elif arg == "--format":
            print_format_info()
            sys.exit()
        elif arg == "--help":
            print_help()
            sys.exit()
        elif arg == "--and":
            control_string = "and"
        elif arg == "--or":
            control_string = "or"
        elif arg == "--not":
            control_string = "not"
        elif arg == "--impl":
            control_string = "impl"
        else:
            print_err_usage()
            sys.exit()
    # if control_string remains modified there was no appropriate input file specified
    # for some option
    if control_string != "":
        print_err_usage()
        sys.exit()

def print_format_info():
    print("\nPliki z wlasnymi wartosciami dla funkcji logicznych musza zawierac po jednej")
    print("linii dla kazdej kombinacji wejsciowych zmiennych logicznych. Format kazdej\nlinii musi byc nastepujacy: ")
    print("\nzmienna1 zmienna2 wynik")
    print("\nUwaga - dla funkcji dla ktorych kolejnosc zmiennych nie jest wazna (np. AND),")
    print("nalezy mimo wszystko zawrzec obie linie.")
    print("Niezastosowanie sie do opisanego formatu bedzie prowadzic do niepoprawnego\ndzialania gry.")

def print_err_usage():
    print("Wystapil blad. Uzyj polecenia --help zeby uzyskac wiecej informacji.")

def print_help():
    print("Uzytkowanie: python game.py [opcja1 sciezka1] [opcja2 sciezka2] ...")
    print("Opcje:")
    print("\t--help   Wyswietla te informacje")
    print("\t--format Wyswietla informacje o formacie plikow tekstowych dla\n\t\t funkcji logicznych")
    print("\t--and    Okreslenie sciezki do pliku z wartosciami dla koniunkcji")
    print("\t--or     Okreslenie sciezki do pliku z wartosciami dla alternatywy")
    print("\t--not    Okreslenie sciezki do pliku z wartosciami dla negacji")
    print("\t--impl   Okreslenie sciezki do pliku z wartosciami dla implikacji")
    print("\nKazda opcja poza --help musi miec jako nastepnika sciezke do odpowiedniego pliku")

def play():
    riddles = RiddleEngine()
    system("clear")
    print("GRA W LOGIKE")
    while True:
        print("Wybierz opcje:")
        print("G)raj")
        print("W)yjdz")
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)       # flush stdin
        control_char = raw_input("> ")
        if control_char == 'G' or control_char == 'g':
            system("clear")
            print("Oto wylosowana zagadka:")
            print("\n")
            riddles.get_random_riddle()
            system("clear")
        elif control_char == 'W' or control_char == 'w':
            sys.exit()
        else:
            system("clear")
            print("Wprowadziles nieodpowiednia litere! Sprobuj raz jeszcze =)")


#####################
#                   #
#     Main part     #
#                   #
#####################

init()
initialize_logic(filenames)
play()