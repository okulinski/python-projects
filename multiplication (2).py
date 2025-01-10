#Multiplication Quiz
#Olivia Kulinski
#1.8.2025

#Init
import random

#Function
def multiplication(): #function that allows for multiplication game to begin
    finalscore = 0 # variable that keeps track of the final score
    while True:
        option = input("Choose an option: play, quit")
        if option == "play":
            num1 = random.randint(1,10) #Generates a random number from 1 to 10
            num2 = random.randint(1,10)
            print("What is " + str(num1) + " x " + str(num2) + ":")
            solution = (num1*num2)
            answer = int(input("Input the answer to the multiplication problem: "))
            print("Your answer: " + str(answer))
            if answer == solution:
                print("Good Job!")
                finalscore = finalscore + 1 #after every correct answer, the score increases by 1
            elif answer != solution:
                print("Wrong answer, the correct answer was " + str(solution))
        elif option == "quit": #When player chooses to quit, they're final score is displayed
            print("Okay, thanks for playing!")
            print("Your final score was " + str(finalscore))
            break


#Main
print("Welcome to the Multiplication Quiz!")
print("Solve the random multiplicatiuon questions and earn points.")
multiplication()
