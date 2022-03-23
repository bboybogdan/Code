x = int(input("Introdu numarul minim de la cat sa inceapa intervalul: "))
y = int(input("Introdu numarul maxim pana la cat sa fie intervalul: "))

for num in range(x,y):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print(num)
