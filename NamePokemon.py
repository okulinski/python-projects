#Pokemon
#Olivia Kulinski

#Init
import random
#Global Variables
pokemon_level = 0
pokemon_name = "Charmander"
day = 1
#Function
def draw_charmander():
    print("""⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬛🟧⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬛🟧🟧⬛⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬜⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜
⬜⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🟧⬛🟧🟧⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟨🟨🟨⬛⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧🟧🟧⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_charmeleon():
    print("""⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬛🟥🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟥⬛⬜⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬜⬜
⬜⬜⬜⬛⬛🟥🟨⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬛⬛🟥🟥⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜
⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛⬛🟥🟥🟥⬜⬛🟥🟥🟥🟥🟥⬛
⬛🟥🟥🟥⬛⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬛⬛🟥🟥🟥🟥⬛
⬛🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥🟥⬛⬜
⬛⬛🟥🟥🟥⬛🟥🟥🟥⬛🟥🟥🟥🟥⬛🟥🟥🟥⬛⬛⬜⬜
⬜⬛🟥🟥🟥🟥🟥⬛🟥⬛🟥🟥🏻🏻⬛⬛⬛⬛🟥🟥⬛⬜
⬜⬜⬛🟥⬛🟥🟥⬛🟥⬜⬛🏻🏻🏻⬛⬜⬜⬛🟥🟥⬜⬛
⬜⬜⬜⬛⬛🟥🟥⬛🟥🟥🟥⬛🏻⬛⬜⬜⬜⬜⬛⬜🟥⬛
⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥⬜⬛🏻⬛⬛⬜⬜⬜⬜⬛⬛⬜
⬜⬜⬜⬜⬛⬛🟥🟥🟥⬛⬛🏻⬛🟥⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟥🟥🟥🟥⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🟥⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_charizard():
    print("""⬜⬜⬜⬜🟥🟥🟥🟨🟨🟨🟨🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟥🟥🟥🟨🟥🟨🟥⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🟥🟥🟧🟥🟨🟨⬜⬛🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜🟧🟧⬜🟥⬜⬜⬜🟥⬜🟧⬛⬜⬜⬜⬜⬜⬜🟧🟧🟧⬜⬜⬜
⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜🟥⬜⬛🟥🟥🟥🟧⬛⬜⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜
⬜⬜⬜🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬛🟥🟥🟧⬛⬛⬜⬜⬜⬜🟧🟦🟧🟧🟧⬜
⬜⬜⬜🟧🟧🟦🟧⬜⬜⬜⬜🏻🏻🏻🟥🟫🟧⬜⬛⬜⬜⬜🟧🟧🟦🟦🟦🟧⬜
⬜⬜🟧🟧🟦🟦🟧🟧⬜⬜⬜⬛🟪🏻🏻🟫🟧🟧🟧⬛⬜⬜🟧🟦🟦🟦🟦🟧🟧
⬜⬜🟧🟦🟦🟦🟧🟧⬜⬜⬛🟧⬛⬛⬛🟧🟧⬛🟧⬛⬜🟧🟧🟦🟦🟦🟦🟦🟧
⬜🟧🟧🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧🟧⬛⬛🟧🟧⬛🟧🟧🟦🟦🟦🟥🟦🟧
⬜🟧🟦🟦🟦🟦🟧🟧⬜⬜⬜⬜⬛⬛⬛🟧⬛⬜⬛⬛⬛🟧🟦🟦🟥🟥🟦🟦🟧
🟧🟧🟦🟦🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧⬛⬜⬜⬜🟧🟧🟦🟦🟥🟨🟦🟦🟥
🟧🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬜⬛🟧🟧🟧⬛⬜⬜🟧🟧🟦🟦🟥🟥🟦🟥🟥🟥
🟧🟦🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬛🟧🟧🟧⬛⬜🟧🟧🟧🟦🟦🟥🟨🟥🟨🟥🟧
🟧🟦🟦⬛⬜⬛🟦🟦🟦🟧🟧⬛🟧🟧🟧🟧⬛🟧🟧🟧🟦🟦🟦🟥🟨🟨🟥🟧🟥
🟧🟦⬜⬜🟧⬜⬛🟦🟦🟧⬛🟧🟧🟧🟧🟧🟧⬛🟧🟧🟦🟦🟥🟨🟨🟨🟨🟥🟧
🟧⬜⬜⬛🟧🟧⬛🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧⬛🟧🟦⬜⬜⬛🟥🟧🟨🟨🟧🟥
🟧⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🏻🏻🏻🏻🟧🟧🟧⬛🟦⬛🟧⬜🟥🟥🟧🟨🟨🟥
⬜⬜⬜⬜⬜⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛🟦⬛🟧⬛🟥🟦
⬜⬜⬜⬜⬛⬛⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧🟧⬛🟦⬜⬛🟧⬛⬜🟦
⬜⬜⬛⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛⬛⬛🟦⬜⬛🟧🟧⬛⬜⬜
⬜⬛🟧🟧🟧🟧⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧⬛⬛🟧🟧⬛⬜⬜⬜
⬜⬛🟧🟧🟧⬛🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜
⬜⬛🟧🟧⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛⬜⬜⬜⬜⬜
⬜⬛🏻🟧⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬛🏻🏻🏻⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬛⬛🟧🟧🟧⬛🏻⬛⬛⬛⬛⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜🟧🟧🟧🟧⬛🏻🏻🏻⬛⬜⬜⬜⬛🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜""")

def train():
    global pokemon_level
    ans = input("Would you like to start your training?: ")
    if ans == "yes":
        pokemon_level = pokemon_level + 1
        print("Your Pokemon level is " + str(pokemon_level))
        while True:
            ans2 = input("Train Again? ")
            if ans2 == "yes":
                pokemon_level = pokemon_level + 1
                print("Your Pokemon level is " + str(pokemon_level))
            if ans2 == "no":
                print("Okay, your pokemon level is " + str(pokemon_level))
                break
    elif ans == "no":
        print("Okay, your pokemon level is " + str(pokemon_level))
        day == day + 1
        print("You are now on day " + str(day))


def gym_battle():
    print("Welcome to the battle field")
    print("Are you ready to begin your battle?")
    ans = input("Are you ready to begin your battle?: ")
    if ans == "yes":
        outcome = random.randint(1,2)
        if outcome == 1:
            print("Great Job you won your battle!")
        elif outcome == 2:
            print("Sorry you lost...")



def rest():
    print("It's time for a break")
    print("Check out your info.")
    if pokemon_level < 5:
        pokemon_name == "Charmander"
        print("Your name is Charmander")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_charmander()
    elif pokemon_level >= 5 and pokemon_level < 10:
        pokemon_name == "Charmeleon"
        print("Your name is now Charmeleon")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_charmeleon()
    elif pokemon_level >= 10:
        pokemon_name == "Charizard"
        print("Your name is now Charizard")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_charizard()

#Main
print("Welcome to Pokemon Evolution")
while True:
    print("Choose an activity for Day: " + str(day))
    print("""
    1.Train
    2. Gym Battle
    3. Rest(Display Info)
    4. Quit
    """)

    activity = int(input("Activity for the day: "))
    if activity == 1:
        print("Welcome to the training quarters")
        print("Train your pokemon in order for it to level up.")
        train()
        global pokemon_name
        day = day + 1
        print("You are now on day " + str(day))

    elif activity == 2:
        gym_battle()
        day = day + 1
        print("You are now on day " + str(day))
    elif activity == 3:
        rest()

    elif activity == 4:
        print("Thanks for playing Pokemon Evolution!")
        break




#Main
#draw_charmander()
#draw_charmeleon()
#draw_charizard()
