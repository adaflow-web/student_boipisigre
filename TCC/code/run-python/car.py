class Voiture(object):
    """ avec quatre caractéristiques
        couleur,
        nom,
        puissance
        vitessemax.
    """

    def __init__(self, couleur , nom, puissance, vitessemax):

        self.couleur = couleur # string
        self.nom = nom #string
        self.puissance = puissance # int
        self.vitessemax = vitessemax # int

    def print(self):
        print ("caractéristiques technique de la voiture : " + self.nom)

        print ("Puissance : " + str(self.puissance)+ " Chevaux")
        print(" Vitesse max : "+ str(self.vitessemax ))

    def drive(self, vitesse) :
        if vitesse <= self.vitessemax:
            print (" une "+ self.nom + " roule à "+ str(vitesse)+ " kmh")
        else:
            print (" vitesse supérieure à la vitesse max de : "+ str(self.vitessemax)+ " kmh")

    def printcolor(self):
        print(" couleur : "+ self.couleur )


v1= Voiture("rouge", "C3",16, 210)

v1.print()
v1.printcolor()
v1.drive(88)
v1.drive(300)
