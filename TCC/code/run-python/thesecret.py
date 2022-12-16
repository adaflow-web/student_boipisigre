lesecret=("Pierre")
print("vous avez droit à 5 essais")
i=1
test = True
while test  :

    entré = input("Un prénom bien connu ")

    if (lesecret == entré) :
        print ("Bravo")
        #break
        test=False
    else :
        print("Désolé ce n'est pas  " + entré)
        print("essai " + str(i) )
    i=i+1

    if i == 6 :
        print("relancer le programme")
        test = False

if i < 6 or i> 6 :
    print("c'est fini")
exit
