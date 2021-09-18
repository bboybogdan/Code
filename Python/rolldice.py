import random

x = str(input("Roll dice?"))
while x == "yes":
	print(random.randrange(1,7))
	break
