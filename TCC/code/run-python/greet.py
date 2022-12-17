def greet(name, age):
    message = "Your name is" + name + " and you are " + int(age) + " years old."
    return message

name = input("Enter your name: ")
age = input("Enter your age: ")

print(greet(name, age))
