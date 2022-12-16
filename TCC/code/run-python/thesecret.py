lesecret=("Pierre")
print("vous avez droit à 5 essais")
i=1

while i < 6 :

    entré = input("Un prénom bien connu ")

    if (lesecret == entré) :
        print ("Bravo")
        break
    else :
        print("désollé ce n'est pas  " + entré)
        print("essai " + str(i) )
    i=i+1

if i == 6 :
    print("relancer le programme")

exit
