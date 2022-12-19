import random

'''
initialisation
nombre secret random number entre  1 et 100
gagné à False
'''

secret = random.randint(1, 100)
gagné = False
essai = 0

while (!gagné) :
    entré = input("donné un nombre en tre 1 et 100 : ")
    nombre = int(entré)

    try:
        essai++
        if nombre == secret :
            gagné = True
            
        if nombre < secret:
            print("nombre plus petit")
        else:
            print("nombre plus grand")

    except Exception as e:
        print("ce n'est pas un nombre, faite attention")
        quit()

print( " Bravo vous avez gagné en "+ str(essai)+" .")
