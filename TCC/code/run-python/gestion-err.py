nombre = input("Type a number: ")

try:
    result = int(nombre) + 1
    pass
except Exception as e:
    print(" pas un nombre")
    quit()

print("The result is " + str(result))
