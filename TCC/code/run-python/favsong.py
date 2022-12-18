
# from goto import goto

Songs=["les vieux","Brave Margot", "Marseille", "Léa"]

print("Boucle 1")
for i in range(4):
    print("chanson " + str(i+1)+" " + Songs[i])

print("Boucle 2")
for chanson in Songs:
    print(chanson)

print("Boucle 3")
i=0
while (i < 4) :
    print("chanson " + str(i+1)+" " + Songs[i])
    i=i+1
    
"""
print("boucle en mode Fortran IV")
i=0
#("hi")
if (i < 4):
    print("chanson " + str(i+1)+" " + Songs[i])
    i=i+1
    goto("hi")
"""
