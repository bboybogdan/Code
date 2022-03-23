import time
import random
from sys import exit

apa = random.randrange(0,2)
if apa == 0:
    print("Trebuie sa pui apa in espresor")
    exit()
elif apa == 1:
    print("Nu trebuie sa pui apa in espresor")
print("Cine vrea sa-si faca cafea? \n1.Bobo. \n2.Mami. \n3.Tati.")

cafea = int(input("Optiune: "))

if cafea == 1:
    print("Cafeaua pentru Bobo va fi gata in 3 minute.")
    time.sleep(3)
    print("Cafeaua lui Bobo este gata.")

if cafea == 2:
    print("Cafeaua pentru mami va fi gata in 3 minute.")
    time.sleep(3)
    print("Cafeaua lui mami este gata.")

if cafea == 3:
    print("Cafeaua pentru tati va fi gata in 3 minute.")
    time.sleep(3)
    print("Cafeaua lui tati este gata.")
