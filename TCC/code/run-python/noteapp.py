

# fonction ouverture du fichier
#
def ouvrefic(nomfic,action):

    if action == "a":
        fichier=open(nomfic,action)
    else
        fichier=open(nomfic)

    return fichier

# fonction fermeture du fichier
def fermefic(fichier):
    fichier.close

# Saisie de la note et ajout de lo NOTE:
def addnote(file):
    saisie = input("saisie du note")
    if saisie != "" :
        file.write(saisie)

        

# fonction de recherche
def rechernote(fichier):
    saisie = input("saisie du mot rechercher")
    i=0
    for ligne in fichier:
        mots=line.split(" ")
        for mot in mots:
            if mot == saisie:
                print (ligne+"\n-----")
                i=i+1
    return i



# initialisation
Fichiernote = "mesnotes.txt"

# Boucle infini sur Choix de l'action

while 1==1 :
    print( "S pour saisir une note \n R pour rechercher une note \n Q pour quitter l'application")
    réponse = input ("S/R/Q")

    if réponse == "Q" or réponse == "q" :
        break

    if réponse == "S" or réponse == "s" :
        filenote=ouvrefic(Fichiernote,"a")
        addnote(filenote)
        fermefic(filenote)

    if réponse == "R" or réponse == "r" :
        filenote=ouvrefic(Fichiernote)
        print(" résultat : \t nombre de notes trouvées"+ rechernote(filenote) + "\n -------")
        fermefic(filenote)
