
#Nome
name = input("Ciao, sono Sofia. Come ti chiami?: ")
print("Piacere di conoscerti, " + name + "! ")

#Amicizia
amico = input("Ti va di fare amicizia, " + name + "? ")

if not amico == "si":
    print("Sarà per la prossima, " + name)
    quit()
else: print("Ok, continuiamo! ")

#Età, Scuola/Lavoro
age = int(input("Quanti anni hai? "))
age += 0

if age < 18:
    print("Sei minorenne! Tranquillo, crescerai.")
    scuola = input("Vai a scuola? ")
    if scuola == "si":
        input("Cosa studi? ")
        print("Ottima scelta! ")
    elif scuola == "no":
        print("Fa niente, non serve a nulla. ")

elif age >= 18 and age <= 30:
    print("Sei maggiorenne! Beato te, sei ancora giovane.")
    lavoro = input("Hai un lavoro? ")
    if lavoro == "si":
        input("Che lavoro fai? ")
        print("Bello, spero che tu riesca a guadagnare molti soldi!")
    elif lavoro == "no":
     print("Tranquillo, lo troverai!")

elif age >=31 and age <= 59:
    print("Sei già maturo, spero tu abbia trovato un lavoro!")

elif age >= 60 and age <=90:
    print("Sei anziano, bello non fare niente eh!")

elif age >= 91:
    print("Sei decrepito, hai ancora poco da vivere!")

#Altezza
altezza = int(input("Quanto sei alto in cm?: "))
altezza += 0

if altezza <= 160:
    print("Sei alto " + str(altezza) + " cm. Sei basso!")
elif altezza >= 170 and altezza <= 180:
    print("Sei alto " + str(altezza) + " cm. Sei normale!")
elif altezza >=181:
    print("Sei alto " + str(altezza) + " cm. Sei alto!")

#Città
città = input("Da dove vieni? ")
print("Che bella! Mi piacerebbe visitarla un giorno.")

#Fidanzata
dama = input("Hai per caso una ragazza, " + name + "? ")
if dama == "si":
    ragazza = input("Uuuh, come si chiama?")
    ragazza2 = input("Mi raccomando, condividi con gli amici! ")
    print("D'accordo, andiamo avanti? ")
else: print("Non importa, le ragazze sono inutili.")

#Hobby/Sport
sport = input("Pratichi qualche sport? ")
if sport == "si":
    input("Che sport? ")
    print("Buon per te, tieniti in forma!")
    hobby2 = input("Hai qualche hobby?")
    if hobby2 == "no":
        print("Vabbè, non sono importanti.")
    elif hobby2 == "si":
        input("Quale? ")
        print("Bello, deve essere divertente!")
elif sport == "no":
    hobby = input("Ah, allora hai un hobby? ")
    if hobby == "si":
        input("Quale? ")
        print("Bello, mi piacerebbe provare un giorno! ")
    elif hobby == "no":
        print("Tranquillo, non devi averne per forza.")

#Colore Preferito
colore = input("Qual è il tuo colore preferito? ")
print("Bel colore!")

#Cibo Preferito
cibo = input("Qual è il tuo cibo preferito? ")
print("Mhh, che bonta! Mi fai venire fame!")

#Musica
musica = input("Che genere di musica ascolti? ")
if musica == "rap":
    eminem = input("Wow, conosci Eminem? ")
    if eminem == "si":
        print("Sei un boss allora!")
    elif eminem == "no":
        print("Ma come! Dovresti ascoltare delle sue canzoni!")
else: print("Vedo che hai dei buoni gusti musicali!")

#Frollo
frollo = input("Ma tu conosci mica il frollo? ")
if frollo == "si":
    print("Benvenuto tra noi!")
else: print("Non sei degno di parlarmi"), quit()

#Cat is Fat
quiz =input("Posso farti una domanda? ")
if quiz == "si":
    cat = input("Is cat fat? ")
    if cat == "yes":
        print("sex")
    else: print("don't masturbate")

