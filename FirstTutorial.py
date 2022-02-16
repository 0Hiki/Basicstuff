
#first_name = "Hiki"
#last_name = "Komori"
#full_name = first_name +" "+ last_name
#print("Hello "+full_name)
#print(type(name))

#age = 15 #senza "" perche senno e' una stringa e non si puo usare per calcoli fa parte della classe int
#age += 1
#print("Your age is: "+str(age))   #per far vedere un altro tipo di dato in stringa fare la cosa precedente
#print(type(age))

#height = 175.5
#print("Your height is: "+str(height)+"cm")
#print(type(height))   #tipo di dato float

#human = Truef        #Boolean meglio delle string
#print("Are you human?: " +str (human))
#print(type(human))




#multiple assignment

#name = "Hiki"
#age = 15
#attractive = True

#name, age, attractive = "Hiki", 15, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30

#Spongebob = Patrick = Sandy = Squidard = 30

#print(Spongebob)
#print(Patrick)
#print(Sandy)
#print(Squidward)



#usefoul string method

#name = "Hiki"
#name = "hiki"

#print(len(name)) #lunghezza nome
#print(name.find("i"))   #a che numero e' la lettera
#(name.capitalize()) #Maiusc sulla prima lettera
#print(name.upper())
#print(name.lower())
#print(name.isdigit()) #se e un digitale
#print(name.isalpha()) se contiene solo lettere
#print(name.count("i"))
#print(name.replace("i","a"))
#print(name*3) #printa il mio nome tot volte


#type casting converti data in other value

#x = 1   #int
#y = 2.0 #float
#z = "3" #str

#int(y)
#x = float(x)
#x = str(x)
#y = str(y)
#z = str(z)
#y = int(y)
#z = int(z)

##print(y)
#print(int(y))
#print(z*3)
#print(z)
#print(z*3)

#print("X is "+str(x))
#rint("Y is "+str(y))
#print(z*3)


#input and shit

#name = input("What is your name?: ")
#age = input("How old are you?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#age = age + 1

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print ("You are "+str(height) + " cm tall")


#Funzioni matematiche

#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))  #arrotonda il numero
#print(math.ceil(pi)) #arrotonda al numero piu grande
#print(math.floor(pi)) #arrotonda al numero piu piccolo
#print(abs(pi)) #valore assoluto di un numero (per esempio se -3.14 ti rida 3.14)
#print(pow(pi,2)) #valore alla seconda ecc
#print(math.sqrt(pi)) #radice quadrata
#print(max(x,y,z)) #valore massimo presente fra numeri evidenziati
#print(min(x,y,z)) #valore minimo presente fra numeri evidenziati


#string slicing
#slicing = creare una sottostringa estraendo pezzi da un'altra stringa
#                   indexing[] o slicing()
#                   [start:stop:step]

#name = "Hiki Ale"

#first_name = name[0:4]   #da lettera a lettera se selezionato 1 solo numero prende la lettera menzionata
#surname = name [5:8]     #puo iniziare da dopo ad esempio dalla 5ta lettera in questo caso Ale
#full_name = first_name +" "+ surname #il nome con il cognome
#nome_strano = name[0:8:2]  #la terza variabile (in questo caso 2) fa vedere solo le lettere ogni 2 dalla prima (puoi ande lasciare start e stop vuoti)
#nome_reversed = name[::-1]

#print(full_name)
#print(nome_strano)
#print(nome_reversed)

#website1 = "https://www.youtube.com"
#website2 = "https://www.pornhub.com"

#slice = slice(12,-4)

#print(website1[slice])
#print(website2[slice])

#If statements

#age = int(input("Quanti anni hai?: "))

#if age >= 100:
#    print("Sei decrepito!")
#elif age >= 18:
#    print("Sei maggiorenne!")
#elif age < 0:
#    print("Sei un coglione!")
#else:
#    print("Sei un bambino!")

#logical operators (and, or, not) = usato per controllare se due o più frasi condizionali sono vere


#temp = int(input("Che tempo fa' fuori?: "))

#if temp >= 0 and temp <= 30:             #questo e quello
    #print("Oggi e' una bella giornata!")
    #print("Esci pure!")
#elif temp < 0 or temp >30:               #questo o quello
#    print("La temperaura e' terribile!")
 #   print("Resta a casa!")

#if not() e elif not() invertono la funzione quindi se applicata al nostro codice a - 20 dira' bella giornata!



#il loop dei while = un affermazione che si ripete finche' e' vera

#while 1==1 :
#    print("Aiuto sono bloccato in un loop!")

#name == " "

#while len(name) == 0:
#    name = input("Scrivi il tuo nome: ")

#print("Ciao "+name)

# for loop = una affermazione che si ripete un numero limitato di volte


#for i in range(10):    #aggiungendo + 1 il raggio aumenta a 10
    #print(i+1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Hiki Ale":
    #print(i)

#import time

#for seconds in range(10,0,-1):   #mettendo -1 inizia dal numero finale
 #   print(seconds)
  #  time.sleep(1)
#print("Buon anno!")

#nested loops= un loop dentro un loop! (loop iniziale e loop finale)

#righe = int(input("Quante righe?: "))
#colonne = int(input("Quante colonne?: "))
#simbolo = input("Scegli un simbolo: ")

#for i in range(righe):
     #for j in range(colonne):
     #   print(simbolo, end="")   #si mette , end="" per non fare muovere il cursore sulla prossima linea
     #print()
