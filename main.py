num_1 = int(input("What is the first number?: "))
num_2 = int(input("What is the  second number?: "))
operation = input("Choose an operation (add, subtract, multiply): ")
def add():
    print str(num_1) + " + " + str(num_2) + " = " + str(num_1 + num_2) 
def subtract():
    print str(num_1) + " - " + str(num_2) + " = " + str(num_1 - num_2) 
def multiply():
    print str(num_1) + " * " + str(num_2) + " = " + str(num_1 * num_2) 
if operation == "add":
    add()
elif operation == "subtract":
    subtract()
elif operation == "multiply":
    multiply()
else:
    print "Invalid operation"