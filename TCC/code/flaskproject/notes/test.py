
def get_notes():
    notesdb=open("static/lesnotes.txt")
    note = notesdb.read()
    notesdb.close()
    notes=note.splitlines()
    return  notes


lesnotes=get_notes()
change_value=""
print(len(lesnotes))
for note in lesnotes:
    #if (note != "") :
    champs=note.split("€")
    print(champs[0])
    #change_value=change_value + "<p>" + champs[0] + "</p> <p>" + champs[1] + "</p>"
    print (champs[1])
