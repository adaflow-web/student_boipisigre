
"""
pour avoir des dates.

import datetime

x = datetime.datetime(2020, 5, 17)
"""
class Note(object):
    """docstring for Note."""

    def __init__(self, numero, createur, texte):
        super(Note, self).__init__()
        self.createur = createur
        self.texte = texte
        self.numero = numero
        self.creation = "01.01.1900"
        self.modification = "02.01.1900"

note1= Note(1,"pierre","mon texte")
note2 =  Note(2,"paul","une note    bizarre")


print ("la note "+ str(note1.numero)+ " : " + note1.texte + " elle a été créée par " + note1.createur)
print (note1.creation)
print ("la note "+ str(note2.numero)+ " : "  + note2.texte + " elle a été créée par " + note2.createur)
print (note1.modification)
