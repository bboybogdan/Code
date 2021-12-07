note = int(input("Cate note ai? "))
teza = int(input("Vrei media cu teza? 1 = (Da) ; 2 = (Nu) "))
if note == 2:
    if teza == 1:
        print("Ce note ai? ")
        n1 = int(input())
        n2 = int(input())
        nt = int(input("Ce nota ai in teza? "))
        media_notelor = (n1 + n2)/2
        media_finala = (3*media_notelor + nt)/4
        print("Media finala este: ",media_finala)
    if teza == 2:
        print("Ce note ai? ")
        n1 = int(input())
        n2 = int(input())
        media_notelor = (n1 + n2)/2
        print("Media finala este: ", media_notelor)
if note == 3:
    if teza == 1:
        print("Ce note ai? ")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        nt = int(input("Ce nota ai in teza? "))
        media_notelor = (n1 + n2 + n3)/3
        media_finala = (3*media_notelor + nt)/4
        print("Media finala este: ", media_finala)
    if teza == 2:
        print("Ce note ai? ")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        media_notelor = (n1 + n2 + n3)/3
        print("Media finala este: ", media_notelor)
