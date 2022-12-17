def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

num_one = input("Enter a number: ")
num_two = input("Enter another number: ")

message = "The result of " + num_one + " + " + num_two + " is " + str(add(int(num_one), int(num_two)))
print(message)

message = "The result of " + num_one + " - " + num_two + " is " + str(subtract(int(num_one), int(num_two)))
print(message)
