#Simple Calculator
#Olivia Kulinski
#11.19.2024

#Init

#Function
#Adds num1 and num2 and prints the results
def add (num1, num2):
    ans = num1 + num2
    print("The result is: " + str(ans))

def subtract(num1, num2):
    ans = num1 - num2
    print("The result is: " + str(ans))

def multiply (num1, num2):
    ans = num1 * num2
    print("The result is: " + str(ans))

def divide (num1, num2):
    ans = num1 / num2
    print("The result is: " + str(ans))

#Main
print("Welcome Preschoolers to Simple Calculator")
while True:
    print("Please choose an operation:")
    print ("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")

    operation = int(input("(1-5) : "))
    if operation == 1:
        add1 = int(input("Enter first number: "))
        add2 = int(input("Enter second number: "))
        add(add1, add2)

    elif operation == 2:
        sub1 = int(input("Enter first number: "))
        sub2 = int(input("Enter second number: "))
        subtract(sub1, sub2)

    elif operation == 3:
        mult1 = int(input("Enter first number: "))
        mult2 = int(input("Enter second number: "))
        multiply(mult1, mult2)

    elif operation == 4:
        div1 = int(input("Enter first number: "))
        div2 = int(input("Enter second number: "))
        divide(div1, div2)

    elif operation == 5:
        print("Thanks for using the simple calculator!")
        break
