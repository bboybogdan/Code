import random

alegere = str(input("Alege: Piatra(p), Forfeca(f), Hartie(h) -> "))
n = random.randrange(1,4);

if n == 1:
    if alegere == "p":
        print("Alegerea mea este piatra. Egalitate.")
    elif alegere == "f":
        print("Alegerea mea este piatra. M-ai batut.")
    elif alegere == "h":
        print("Alegerea mea a fost piatra. Te-am batut.")
elif n == 2:
    if alegere == "p":
        print("Alegerea mea a fost foarfeca. M-ai batut.")
    elif alegere == "f":
        print("Alegerea mea a fost foarfeca. Egalitate.")
    elif alegere == "h":
        print("Alegerea mea a fost foarfeca. Te-am batut.")
elif n == 3:
    if alegere == "p":
        print("Alegerea mea a fost hartie. Te-am batut.")
    elif alegere == "f":
        print("Alegerea mea a fost hartie. M-ai batut.")
    elif alegere == "h":
        print("Alegerea mea a fost hartie. Egalitate.")
