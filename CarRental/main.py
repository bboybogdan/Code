stockmustang = {
    "mustangstock" : 1
}

stockopel = {
    "opelstock" : 1
}

aprovizionaremasini = {
    "aprovizionare" : 0
}

optiune_model = str(input("Alegeti modelul dorit de masina dintre Musntag si Ford "))
if optiune_model == "Mustang":
    if stockmustang["mustangstock"] >= 1:
        print("Masina Mustang este valabile")
        stockmustang["mustangstock"] = stockmustang["mustangstock"] - 1
    elif stockmustang["mustangstock"] < 1:
        print("Masina Mustang nu este valabila. O sa reaprovizionam in scurt timp")
        stockmustang["mustangstock"] = stockmustang["mustangstock"] + 10