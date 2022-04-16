from colorama import init, Fore, Back, Style
import random
import re

def obrada_greske(poruka):
    return "Pogresan unos:" + poruka

init()
loop = True
word_list = ['farsu', 'jedan', 'uspeh', 'forda', 'istoj', 'kojoj', 'dobri', 'svejk', 'jedna', 'farsa']

while loop:
    print(Back.WHITE + Fore.BLACK + "Zelis li da igras? (da/ne)" + Style.RESET_ALL)
    command = input()
    if command == "ne":
        loop = False
    elif command == "da":
        inner_loop = 0
        word = random.choice(word_list)
        print("Unesi rec, ali pazi rec mora biti 5 slova ili vise!")

        counter = 29

        while inner_loop < counter:

            attempt = input("Unesi rec:")
            
            if len(attempt) != 5:
                print(obrada_greske("invalid length"))
                continue

            # Logika igre
            output = ""
            for i in range(word.__len__()):
                if attempt[i] == word[i]:
                    counter-=1
                    output = output + Back.RED + attempt[i] + Back.RESET
                elif attempt[i] in word[i]:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET
                    counter-=1
                else:
                    output = output + attempt[i] + Back.RESET
                    counter-=1
            print(output)
            
            if word == attempt:
                print("Cestitamo domacine, vidim gleda se slagalica")
                quit()

        print("Izgubio si tacna rec je bila:", word)
