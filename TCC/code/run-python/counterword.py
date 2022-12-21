text_file = open("zen.txt")
nbmots=0

for line in text_file:
    # print(line)
    newline=line.replace("is", "should be")
    print(newline.upper())
    lines=line.rstrip()
    mots = lines.split(" ")
    nbmots=nbmots+len(mots)

print("nombre de mots " + str(nbmots) )


text_file.close()
