

# fonction ouverture du fichier
#
def ouvrefic(nomfic,action):

    if action == "Ecriture":
        fichier=open(nomfic,"a")
    else:
        fichier=open(nomfic)

    return fichier

# fonction fermeture du fichier
def fermefic(fichier):
    fichier.close

# Saisie de la note et ajout de lo NOTE:
def addnote(file):
    saisie = input("saisie d'une note : ")
    if saisie != "" :
        file.write(saisie+"\n")

def nettoie(content):
    words = content.replace( "-" ,"").replace( "*", "").replace(",", "").replace(".", "").replace("!", "").replace("'", "").replace("\n", " ").replace("  ", " ").strip()
    return words
# fonction de recherche
def rechernote(fichier):
    saisie = input("saisie du mot rechercher : ")
    i=0
    for ligne in fichier:
        lignepropre= nettoie(ligne)
        mots=lignepropre.split(" ")
        for mot in mots:
#            print (mots)
#            print (mot)
            if mot == saisie:
                print ("\t"+ligne+"\n-----")
                i=i+1
    return str(i)



# initialisation
Fichiernote = "mesnotes.txt"

# Boucle infini sur Choix de l'action

while 1==1 :
    print( "\t S pour saisir une note \n \t R pour rechercher une note \n \t Q pour quitter l'application")
    réponse = input ("S/R/Q : ")

    if réponse == "Q" or réponse == "q" :
        break

    if réponse == "S" or réponse == "s" :
        filenote=ouvrefic(Fichiernote,"Ecriture")
        addnote(filenote)
        fermefic(filenote)

    if réponse == "R" or réponse == "r" :
        print("\t Résultat :")
        filenote=ouvrefic(Fichiernote,"lecture")
        print(" \t nombre de notes trouvées :\t"+ rechernote(filenote) + "\n =========================================")
        fermefic(filenote)

print ("bye bye")
exit(0)
