
"""
pour avoir des dates.

import datetime

x = datetime.datetime(2020, 5, 17)
"""


class Note(object):
    """
    creation d'une classe note  comprenant
        un numero
        une date de création
        une date de modification
        nom du createur
        le texte de la note
    """
    numero = 0
    creation = "01.01.1900"
    modification = "02.01.1900"
    createur = ""
    texte = ""

    def printtext(self):
        return f"{self.texte}"

    def printcreateur(self):
        return f"{self.createur}"

    def printnum(self):
        return f"{self.numero}"



note1 = Note()

note1.numero = 1
note1.creation = "30.12.2022"
note1.modification = "30.12.2022"
note1.createur = "Pierre"
note1.texte = "voici ma premiere note"

note2 = Note()
note2.numero = 2
note2.creation = "30.12.2022"
note2.modification = "30.12.2022"
note2.createur = "Paul"
note2.texte = "voici ma seconde note"

print ("la note "+ str(note1.numero)+ " : " + note1.texte + " elle a été créée par " + note1.createur)
print ("la note "+ str(note2.numero)+ " : "  + note2.texte + " elle a été créée par " + note2.createur)

print("la note " + note1.printnum() +" : "+ note1.printtext()+ " Elle a été créée par "+ note1.printcreateur())
