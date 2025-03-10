print ("Welcome to my Calculator program")
signs = ['+', '-', '*', '/']
result = None

while True:
    ready = input ("Do you want to Continue? (Enter Y or N): ")
    ready = ready.upper()

    if ready == "Y":
        break
            
    elif ready == "N":
        print ("Bye")
        quit ()
    else:
        print ("Please only enter Y or N")
            


number_a = input ("Enter number A: ")
operation = input ("Enter the operation (+, -, *, /): ")
number_b = input ("Enter number B: ")

if number_a.isdigit() and number_b.isdigit():
    number_a = int(number_a)
    number_b = int(number_b)
else:
    print ("Please enter a valid number")



if operation in signs:
    if operation == "+":
        result = number_a + number_b
    elif operation == "-":
        result = number_a - number_b
    elif operation == "*":
        result = number_a * number_b
    elif operation == "/":
        result = number_a / number_b
else:
    print ("Enter a valid operation")
    quit()

print (f"{number_a} {operation} {number_b} = {result}")

    
