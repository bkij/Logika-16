from __future__ import print_function
import random
from os import system
from logic import *


class RiddleEngine:

    MAX_RIDDLE_NUM = 5

    def __init__(self):
        self.riddles = [
            self.riddle1,
            self.riddle2,
            self.riddle3,
            self.riddle4,
            self.riddle5
            ]

    def get_random_riddle(self):
        self.riddles[random.randint(0, RiddleEngine.MAX_RIDDLE_NUM - 1)]()

    def map_answer(self, answer):
        if answer == '1':
            return '1'
        elif answer == '0':
            return '2'
        elif answer == 'X':
            return '3'

    def continue_with_answer(self, correct_answer):
        user_answer = raw_input("> ")
        while user_answer != '1' and user_answer != '2' and user_answer != '3':
            print("Cos poszlo nie tak. Sprobuj jeszcze raz, wpisujac cyfre 1, 2, lub 3")
            user_answer = raw_input("> ")
        if user_answer == correct_answer:
            print("Brawo! Poprawna odpowiedz")
        else:
            print("Niestety odpowiedz jest niepoprawna :(")
            print("Odsylam po wytlumaczenie do kodu zrodlowego")
        system('sleep 4')

    def riddle1(self):
        print("Janusz patrzy na Mariole. Mariola patrzy na Konrada.")
        print("Janusz jest zonaty, a Konrad nie.")
        print("Czy w tej sytuacji prawda jest, ze osoba w zwiazku malzenskim patrzy\nna osobe nie bedaca w takim zwiazku?")
        print("\n")
        print("1) Tak")
        print("2) Nie")
        print("3) Nie mozna okreslic")

        p = '1'                                                             # janusz w zwiazku?
        q = '0'                                                             # konrad w zwiazku?
        #
        #   Mariola jest lub nie jest w zwiazku, bo w prawdziwym zyciu nie ma
        #   niezdefiniowanego stanu cywilnego, r v ~r = 1
        #
        r = '1'                                                             # jedna z mozliwosci 
        answer = custom_or(
                    custom_or(custom_and(p, custom_not(r)), custom_and(r, q)),
                    custom_or(custom_and(p, custom_not(custom_not(r))), custom_and(custom_not(r), q))
                 )
        #
        #   Zagadka ma odpowiedz twierdzaca, jesli janusz jest w zwiazku a mariola nie
        #   lub mariola jest w zwiazku a konrad nie
        #
        self.continue_with_answer(self.map_answer(answer))

    def riddle2(self):
        print("Towarzysz Stalin powiedzial, ze jesli nie ma czlowieka, to nie ma problemu.")
        print("Oczywiscie zakladamy ze mial racje.")
        print("Czy mozemy w takim wypadku powiedziec, ze jesli jest problem,\nto jest rowniez czlowiek?")
        print("\n")
        print("1) Tak")
        print("2) Nie")
        print("3) Nie mozna okreslic")
        p = '1'                         # nie ma czlowieka
        q = '1'                         # nie ma problemu
        answer = custom_impl(
                    custom_impl(p, q),
                    custom_impl(custom_not(q), custom_not(p))
                 )
        self.continue_with_answer(self.map_answer(answer))

    def riddle3(self):
        print("Janusz ma konia.")
        print("Czy mozemy powiedziec, ze posiadanie przez Janusza konia pociaga za soba")
        print("posiadanie konia przez Ale, lub ze posiadanie konia przez Ale")
        print("pociaga za soba posiadanie konia przez Janusza?")
        print("\n")
        print("1) Tak")
        print("2) Nie")
        print("3) Nie mozna okreslic")
        p = '1'                         # Janusz ma konia
        q = 'X'                         # Ala ma konia
        answer = custom_or(
                    custom_impl(p, q),
                    custom_impl(q, p)
                 )
        self.continue_with_answer(self.map_answer(answer))

    def riddle4(self):
        print("Janusz i Grazyna sa rodzenstwem.")
        print("Andzelika i Tadeusz rowniez sa rodzenstwem.")
        print("Janusz ma anakonde.")
        print("Andzelika nie ma zadnego zwierzatka.")
        print("Wszyscy pozostali czlonkowie obu rodzin nie zyja.")
        print("Czy prawda jest, ze w jednej i drugiej rodzinie jest co najmniej jedno zwierze?")
        print("\n")
        print("1) Tak")
        print("2) Nie")
        print("3) Nie mozna okreslic")
        p = '0'         # andzelika nie ma zwierzaka
        q = 'X'         # taduesz - nie wiadomo
        r = 'X'         # grazyna - nie wiadomo
        s = '1'         # janusz ma zwierzaka
        answer = custom_and(
                    custom_or(r, s),
                    custom_or(p, q)
                 )
        self.continue_with_answer(self.map_answer(answer))

    def riddle5(self):
        print("Adam lubi truskawki. Konrad i Kasia nie lubia truskawek.")
        print("Kasia nigdy w zyciu nie jadla truskawek.")
        print("Czy mozemy powiedziec, ze jednoczesnie albo Adam albo Monika lubia truskawki")
        print("i Monika lubilaby truskawki, wtedy i tylko wtedy, gdy Kasia lubi truskawki?")
        print("\n")
        print("1) Tak")
        print("2) Nie")
        print("3) Nie mozna okreslic")
        p = '1'         # Adam lubi truskawki
        q = 'X'         # Monika - nie wiadomo
        r = '0'         # Konrad nie lubi truskawek
        s = '0'         # Kasia tez
        answer = custom_and(
                    custom_xor(p, q),
                    custom_and(
                        custom_impl(s, q),
                        custom_impl(q, s)
                    )
                 )
        self.continue_with_answer(self.map_answer(answer))


