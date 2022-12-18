"""

    Sort it by alphabetical order.
    Display each song in it on its own line in the terminal.
    Add a 5th song at the end of the array.
    Display how many songs are in the array inside a sentence such as "There are x songs in the array."
    Remove the 3rd song in the array.
    Display the content of the array on one line.
    Display the length of the array.
"""

Songs=["les vieux","Brave Margot", "Marseille", "Léa"]

# 1
Songs.sort()

# 2
print(Songs)

#3
Songs.append("La montagne")

#4
print("There are " + str(len(Songs)) + " songs in the array.")
print(Songs)
#5
Songs.pop(2)

# 6
for chanson in Songs:
    print(chanson)

#7
print("There are " + str(len(Songs)) + " songs in the array.")
