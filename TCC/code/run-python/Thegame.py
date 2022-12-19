import random

'''
initialisation
nombre secret random number entre  1 et 100
gagné à False
'''

secret = random.randint(1, 100)
#print (secret)
essai = 0

while ( 1 == 1) :
    entré = input("saisir un nombre entre 1 et 100 : ")
        #print (secret, nombre)
    try:
        nombre = int(entré)
        essai = essai +1
        if nombre == secret :
            break

        if nombre < secret:
            print("le nombre plus petit que le secret")
        else:
            print("le nombre plus grand que le secret")


    except Exception as e:
        print("ce n'est pas un nombre, faite attention")
        quit()

print( " Bravo vous avez gagné en "+ str(essai)+" .")
