print("Alege una ditre optiuni: \n1.Calculator.\n2.Consoana sau Voacala. \n3.Numarul lui Fibonacci \n4.Numerele prime(dintr-un interval). \n5.Cmmmdc. \n6.Numarul de cate ori se repete o litera intr-un cuvunt. \n7.Pattern 12. \n8.Numar aleatoriu. \n9.Parola securizata. \n10.Cum sa compilezi un cod python folosind CMD.")
optiune = int(input("Optiune: "))
f = open("rez.out" ,"w")

if optiune == 1:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        num1 = int(input("Introdu primul numar: "))
        num2 = int(input("Introdu al doilea numar: "))
        actiune = int(input("Alege o actiune: Adunare(1), Scadere(2), Inmultire(3), Impartitre(4) -> "))
        print("Rezultatul este: ", end="")
        if actiune == 1:
            print(num1 + num2)
        elif actiune == 2:
            print(num1 - num2)
        elif actiune == 3:
            print(num1 * num2)
        else:
            print(num1 / num2)
    else:
        num1 = int(input("Introdu primul numar: "))
        num2 = int(input("Introdu al doilea numar: "))
        actiune = int(input("Alege o actiune: Adunare(1), Scadere(2), Inmultire(3), Impartitre(4) -> "))
        f.write("Rezultatul este: ")
        if actiune == 1:
            f.write(str(num1 + num2))
        elif actiune == 2:
            f.write(str(num1 - num2))
        elif actiune == 3:
            f.write(str(num1 * num2))
        else:
            f.write(str(num1 / num2))
elif optiune == 2:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        litera = str(input("Introdu o litera din alfabet: "))
        literaMica = (c == "a" or c == "e" or c == "i" or c == "o" or c == "u")
        literaMare = (c == "A" or c == "E" or c == "I" or c == "O" or c == "U")

        if literaMica or literaMare:
            print(litera + " e o vocala")
        else:
            print(litera + " e o consoana")
    else:
        litera = str(input("Introdu o litera din alfabet: "))
        literaMica = (litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u")
        literaMare = (litera == "A" or litera == "E" or litera == "I" or litera == "O" or litera == "U")

        if literaMica or literaMare:
            f.write(str(litera + " e o voacala"))
        else:
            f.write(str(litera + " e o consoana"))
elif optiune == 3:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        numarulDeTermeni = int(input("Introdu numarul de termini pana la cat sa fie numarul lui Fibonacci: "))
        t1, t2 = 0, 1
        count = 0

        if numarulDeTermeni <= 0:
            print("Introdu un numar care sa fie mai mare decat 0")
        elif numarulDeTermeni == 1:
            print("Numerele lui Fibonacci pana la", numarulDeTermeni, ":")
            print(t1)
        else:
            print("Numarul lui Fibonacci: ")
            while count < numarulDeTermeni:
                print(t1)
                s = t1 + t2
                t1 = t2
                t2 = s
                count += 1
    else:
        numarulDeTermeni = int(input("Introdu numarul de termeni pana la cat sa fie numaurl lui Fibonacci: "))
        t1, t2 = 0, 1
        count = 0

        if numarulDeTermeni <= 0:
            f.write(str("Introdu un numar care sa fie mai mare decat 0"))
        elif numarulDeTermeni == 1:
            f.write(str("Numerele lui Fibonacci pana la", numarulDeTermeni, ":"))
            f.write(str(t1))
        else:
            f.write(str("Numarul lui Fibonacci: "))
            while count < numarulDeTermeni:
                f.write(str(t1 ))
                s = t1 + t2
                t1 = t2
                t2 = s
                count += 1
elif optiune == 4:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        x = int(input("Introdu numarul minim de la cat sa inceapa intervalul: "))
        y = int(input("Introdu numarul maxim pana la cat sa fie intervalul: "))

        for num in range(x,y):
            prime = True
            for i in range(2,num):
                if (num%i==0):
                    prime = False
            if prime:
               print(num)
    else:
        x = int(input("Introdu numarul minim de la cat sa inceapa intervalul: "))
        y = int(input("Introdu numarul maxim pana la cat sa fie intervalul: "))

        for num in range(x,y):
            prime = True
            for i in range(2,num):
                if (num%i==0):
                    prime = False
            if prime:
               f.write(str(num))

elif optiune == 5:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        nr1 = int(input('Da primul nr: '))
        nr2 = int(input('Da al doilea nr: '))
        if(nr1 > nr2):
        	nr1=nr1-nr2
        else:
            nr2=nr2-nr1
        print(nr1)
    else:
        nr1 = int(input('Da primul nr'))
        nr2 = int(input('Da al doilea nr'))
        if(nr1 > nr2):
        	nr1=nr1-nr2
        else:
        	nr2=nr2-nr1
        f.write(str(nr1))
elif optiune == 6:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        cuvant = str(input("Introdu cuvantul: "))
        litera = str(input("Intra litera care sa fie cautata: "))
        count = 0

        for ltr in cuvant:
            if ltr == litera:
                count += 1
        print(f"Litera '{litera}' a fost repetata de {count} ori")
    else:
        cuvant = str(input("Introdu cuvantul: "))
        litera = str(input("Intra litera care sa fie cautata: "))
        count = 0

        for ltr in cuvant:
            if ltr == litera:
                count += 1
        f.write(str(f"Litera '{litera}' a fost repetata de {count} ori"))
elif optiune == 7:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
            for x in range (1,6):
                for y in range(1, x+1):
                    print(y, end="")
                print()
    else:
            for x in range (1,6):
                for y in range(1, x+1):
                    f.write(str(y))
                f.write(str())
elif optiune == 8:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
            import random
            x = int(input("Introdu un numar de la cat sa inceapa alegerea unui numar aleatoriu: "))
            y = int(input("Introdu un numar pana la cat se se termine alegerea unui numar aleatoriu: "))
            print(random.randrange(x,y))
    else:
            import random
            x = int(input("Introdu un numar de la cat sa inceapa alegerea unui numar aleatoriu: "))
            y = int(input("Introdu un numar pana la cat se se termine alegerea unui numar aleatoriu: "))
            f.write(str(random.randrange(x,y)))
elif optiune == 9:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        import random
        from string import digits
        from string import punctuation
        from string import ascii_letters

        symbols = ascii_letters + digits + punctuation
        secure_random = random.SystemRandom()
        password = "".join(secure_random.choice(symbols)
                  			for i in range(20))
        print(password)
    else:
        import random
        from string import digits
        from string import punctuation
        from string import ascii_letters

        symbols = ascii_letters + digits + punctuation
        secure_random = random.SystemRandom()
        password = "".join(secure_random.choice(symbols)
        					for i in range(20))

        f.write(str(password))
elif optiune == 10:
    inFisierSauInFolder = int(input("Apasa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): "))
    if inFisierSauInFolder == 1:
        print("Ca sa compilezi un program python folosind CMD ruleaza aceasta comanda in CMD: \npython FILE_NAME.py")
    else:
        f.write(str("Ca sa compilezi un program python folosind CMD ruleaza aceasta comanda in CMD: \npython FILE_NAME.py"))
