#Ohjelman hyväksyvä salasana
nimi = "asd"

#Pyydetään salasana
salasana = input(str("Anna salasana: "))

#määritetään alkiot
jatkuu = False
teksti = "täälä ei ole mitään :/ \n"

if salasana == nimi:
    jatkuu = True

else:
    print("Vaara salasana")
    
while jatkuu:
    valinta = str(input("Mitä haluat tehdä? \n (1) Lue muistio \n (2) Kirjoita muistioon \n (3) Poista muistio \n (4) Sulje muistio:"))
    if valinta == "1":
        print(teksti)
    elif valinta == "2":
        teksti = teksti  + input("Kirjoita tähän:\n ") + "\n"
    elif valinta == "3":
        teksti = ""
    elif valinta == "4":
        jatkuu = False
    else:
        print("In Valid input")
