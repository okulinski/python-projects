#Phoenix Ling,Olivia Kulinski, Matthew Kim, Charlotte Quinn
#Create Task
#March 17 2025


#Init


from PIL import Image
import requests
from io import BytesIO
import random
import time
salads=["Chicken Caeser Salad","Garden Salad","Caprese Salad"]
saladingredients=["chicken,lettuce,crouton,parmesancheese,oliveoil,lemon,worcestershiresauce,mustard,garlic,anchovy","lettuce,tomato,cucumber,olive","tomato,mozzarella,basil,balsamicvinegar"]
saladrestrictions=["none","vegan,vegeterian,glutenfree,lactosefree","vegan,vegetarian"]
sandwiches=["BLT","Gluten Free Grilled Cheese","Club Sandwich","Veggie Sandwich"]
sandwichingredients=["bacon,lettuce,tomato,bread","cheddar,bread","avocado,tomato,lettuce,mayo,bread,chicken,bacon","bread,tomato,redonion,cucumber,lettuce,pepper,oil"]
sandwichrestrictions=["lactosefree","vegetarian,glutenfree","none","vegetarian,vegan,lactosefree"]
soups=["Chicken Noodle Soup","Chili","Tomato Soup"]
soupingredients=["chicken,chickenbroth,noodles,carrot,celery,water","beef,blackbeans,tomato,onion,garlic,corn","tomato,onion,garlic,oliveoil,cream"]
souprestrictions=["glutenfree,lactosefree","glutenfree,lactosefree","glutenfree,vegan,vegetarian"]
drinks=["Still Water","Sparkling Water","Soda","Apple Juice","Orange Juice","Strawberry Banana Smoothie"]
drinkingredients=["water","water","ingredients vary","water,apple","water,orange","strawberry,banana,milk"]
drinkrestrictions=["glutenfree,vegan,vegetarian,lactosefree","glutenfree,vegan,vegetarian,lactosefree","glutenfree,vegan,vegetarian,lactosefree","glutenfree,vegan,vegetarian,lactosefree","glutenfree,vegan,vegetarian,lactosefree","vegitarian,glutenfree"]
recommendeditems=[]
recommendedingredients=[]
finalrecommendations=[]
finalingredients=[]
saladphotolinks=["https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_auto,w_728,h_546/k%2FPhoto%2FRecipes%2F2024-04-chicken-caesar-salad%2Fchicken-caesar-salad-653","https://www.missinthekitchen.com/wp-content/uploads/2020/03/Green-Salad-Recipe-Image-683x1024.jpg","https://www.thespruceeats.com/thmb/QZtRJibA70fH7B5XKodp_1HTS7k=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/caprese-salad-tomato-salad-2217097-hero-03-75a0b89b30aa4a52b10fe4fdd9abfeb5.jpg"]
soupphotolinks =["https://www.bigbearswife.com/wp-content/uploads/2020/05/30-Minute-Pantry-Chicken-Noodle-Soup-3-731x1024.png","https://hips.hearstapps.com/hmg-prod/images/beef-chili-lead-6630087a9ab98.jpg?crop=0.9994794377928162xw:1xh;center,top&resize=1200:*","https://www.allrecipes.com/thmb/jbodaMY5KLc7g5gHmHMT2MUqjvE=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/277311spicy-fresh-tomato-soupFranceC4x3-56454ad082214f33960f62665fc8c169.jpg"]
sandwichphotolinks=["https://dyvn6jpt1f0d3.cloudfront.net/wp-content/uploads/2023/10/14154227/BLT-for-recipe-1-6-980x551.jpeg","https://www.allrecipes.com/thmb/CZ93z2oGv0n9ZsLp5yE2Lgb0Tyk=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/AR-238891-Grilled-Cheese-Sandwich-beauty-4x3-362f705972e64a948b7ec547f7b2a831.jpg","https://www.seriouseats.com/thmb/0nUt5iaqM54mdfbWRv6A8VrP_Yo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/20231204-SEA-TurkeyClub-FredHardy-03-e345fa83f2b4492d8c921d1dbd91a596.jpg","https://www.andiemitchell.com/wp-content/uploads/2019/01/best_veggie_sandwich_hummus_avocado-2.jpg"]
drinkphotolinks=["https://sojo.net/sites/default/files/blog/shutterstock_65621872_0.jpg","https://www.nextlevelurgentcare.com/wp-content/uploads/elementor/thumbs/AdobeStock_233416704-scaled-q7kwpmr1z68b3zzupki2yr9ffad06ve4c0fyj6v5kw.jpeg","https://134532506.cdn6.editmysite.com/uploads/1/3/4/5/134532506/s549469990591119337_p28_i3_w900.jpeg?width=2400&optimize=medium","https://parade.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_700/MjAwNjM4NjE1MDExNzMwODA4/is-apple-juice-good-for-you.webp","https://images-prod.healthline.com/hlcmsresource/images/AN_images/orange-juice-1296x728-feature.jpg","https://www.simplyrecipes.com/thmb/YZRqiGDbKwgaw1ayN6LykaoieAA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Simply-Recipes-Strawberry-Banana-Smoothie-LEAD-2-RECIRC-40ae66e586a341d7951fa38f5659fac4.jpg"]


#Functions

def open_image(url): #function that opens images from the internet
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def saladselection(): #function that selects a salad for the user based off given restrictions
    recommendeditems.clear()
    recommendedingredients.clear()
    print("""Please select your dietary restrictions/choices
(Vegan(V), vegetarian(VG), gluten free(GF), lactose free(LF), or None(N)))""")
    print(" ")
    restriction=input("Enter restriction/choice here:") #user gets to enter their dietary restrictions
    if restriction=="V" or restriction=="v":
        print("Vegan selected")
        print(" ")
        time.sleep(1)
        for i in range(len(salads)): #Goes through the list of salad restrictions and makes sure it satisfies the restriction
            if "vegan" in saladrestrictions[i]:
                recommendeditems.append(salads[i])
                recommendedingredients.append(saladingredients[i])
        print("Generating random salad now...")
        time.sleep(1)
    elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
        print("Vegetarian selected")
        print(" ")
        time.sleep(1)
        for i in range(len(salads)):
            if "vegetarian" in saladrestrictions[i]:
                recommendeditems.append(salads[i])
                recommendedingredients.append(saladingredients[i])
        print("Generating random salad now...")
        time.sleep(1)
    elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
        print("Gluten free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(salads)):
            if "glutenfree" in saladrestrictions[i]:
                recommendeditems.append(salads[i])
                recommendedingredients.append(saladingredients[i])
        print("Generating random salad now...")
        time.sleep(1)
    elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
        print("Lactose free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(salads)):
            if "lactosefree" in saladrestrictions[i]:
                recommendeditems.append(salads[i])
                recommendedingredients.append(saladingredients[i])
        print("Generating random salad now...")
        time.sleep(1)
    else:
        print("No dietary restrictions/choices selected.")
        print(" ")
        print("Generating random salad now...")
        time.sleep(1)
        for i in range(len(salads)):
            recommendeditems.append(salads[i])
            recommendedingredients.append(saladingredients[i])
    randomindex=random.randint(0,(len(recommendeditems)-1))
    generateditem = recommendeditems[randomindex]
    generateditemingredients = recommendedingredients[randomindex]
    print(" ")
    print("Suggested salad: " + generateditem)
    photoindex = salads.index(generateditem)
    open_image(saladphotolinks[photoindex])
    time.sleep(1)
    finalrecommendations.append(generateditem)
    finalingredients.append(generateditemingredients)


def soupselection():
    recommendeditems.clear()
    recommendedingredients.clear()
    print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or lactose free(LF)))")
    print(" ")
    restriction=input("Enter restriction/choice here:")
    if restriction=="V" or restriction=="v":
        print("Vegan selected")
        print(" ")
        time.sleep(1)
        for i in range(len(soups)):
            if "vegan" in souprestrictions[i]:
                recommendeditems.append(soups[i])
                recommendedingredients.append(soupingredients[i])
        print("Generating random soup now...")
        time.sleep(1)
    elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
        print("Vegetarian selected")
        print(" ")
        time.sleep(1)
        for i in range(len(soups)):
            if "vegetarian" in souprestrictions[i]:
                recommendeditems.append(soups[i])
                recommendedingredients.append(soupingredients[i])
        print("Generating random soup now...")
        time.sleep(1)
    elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
        print("Gluten free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(soups)):
            if "glutenfree" in souprestrictions[i]:
                recommendeditems.append(soups[i])
                recommendedingredients.append(soupingredients[i])
        print("Generating random soup now...")
        time.sleep(1)
    elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
        print("Lactose free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(soups)):
            if "lactosefree" in souprestrictions[i]:
                recommendeditems.append(soups[i])
                recommendedingredients.append(soupingredients[i])
        print("Generating random soup now...")
        time.sleep(1)
    else:
        print("No dietary restrictions/choices selected.")
        print(" ")
        print("Generating random soup now...")
        time.sleep(1)
        for i in range(len(soups)):
            recommendeditems.append(soups[i])
            recommendedingredients.append(soupingredients[i])
    randomindex=random.randint(0,(len(recommendeditems)-1))
    generateditem=recommendeditems[randomindex]
    generateditemingredients=recommendedingredients[randomindex]
    print(" ")
    print("Suggested soup: " + generateditem)
    photoindex = soups.index(generateditem)
    open_image(soupphotolinks[photoindex])
    time.sleep(1)
    finalrecommendations.append(generateditem)
    finalingredients.append(generateditemingredients)


def sandwichselection():
    recommendeditems.clear()
    recommendedingredients.clear()
    print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or lactose free(LF)))")
    print(" ")
    restriction=input("Enter restriction/choice here:")
    if restriction=="V" or restriction=="v":
        print("Vegan selected")
        print(" ")
        time.sleep(1)
        for i in range(len(sandwiches)):
            if "vegan" in sandwichrestrictions[i]:
                recommendeditems.append(sandwiches[i])
                recommendedingredients.append(sandwichingredients[i])
        print("Generating random sandwich now...")
        time.sleep(1)
    elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
        print("Vegetarian selected")
        print(" ")
        time.sleep(1)
        for i in range(len(sandwiches)):
            if "vegetarian" in sandwichrestrictions[i]:
                recommendeditems.append(sandwiches[i])
                recommendedingredients.append(sandwichingredients[i])
        print("Generating random sandwich now...")
        time.sleep(1)
    elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
        print("Gluten free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(sandwiches)):
            if "glutenfree" in sandwichrestrictions[i]:
                recommendeditems.append(sandwiches[i])
                recommendedingredients.append(sandwichingredients[i])
        print("Generating random sandwich now...")
        time.sleep(1)
    elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
        print("Lactose free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(sandwiches)):
            if "lactosefree" in sandwichrestrictions[i]:
                recommendeditems.append(sandwiches[i])
                recommendedingredients.append(sandwichingredients[i])
        print("Generating random sandwich now...")
        time.sleep(1)
    else:
        print("No dietary restrictions/choices selected.")
        print(" ")
        print("Generating random sandwich now...")
        time.sleep(1)
        for i in range(len(sandwiches)):
            recommendeditems.append(sandwiches[i])
            recommendedingredients.append(sandwichingredients[i])
    randomindex=random.randint(0,(len(recommendeditems)-1))
    generateditem=recommendeditems[randomindex]
    generateditemingredients=recommendedingredients[randomindex]
    print(" ")
    print("Suggested sandwich: " + generateditem)
    photoindex = sandwiches.index(generateditem)
    open_image(sandwichphotolinks[photoindex])
    time.sleep(1)
    finalrecommendations.append(generateditem)
    finalingredients.append(generateditemingredients)


def drinkselection():
    recommendeditems.clear()
    recommendedingredients.clear()
    print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or lactose free(LF)))")
    print(" ")
    restriction=input("Enter restriction/choice here:")
    if restriction=="V" or restriction=="v":
        print("Vegan selected")
        print(" ")
        time.sleep(1)
        for i in range(len(drinks)):
            if "vegan" in drinkrestrictions[i]:
                recommendeditems.append(drinks[i])
                recommendedingredients.append(drinkingredients[i])
        print("Generating random drink now...")
        time.sleep(1)
    elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
        print("Vegetarian selected")
        print(" ")
        time.sleep(1)
        for i in range(len(drinks)):
            if "vegetarian" in drinkrestrictions[i]:
                recommendeditems.append(drinks[i])
                recommendedingredients.append(drinkingredients[i])
        print("Generating random drink now...")
        time.sleep(1)
    elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
        print("Gluten free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(drinks)):
            if "glutenfree" in drinkrestrictions[i]:
                recommendeditems.append(drinks[i])
                recommendedingredients.append(drinkingredients[i])
        print("Generating random drink now...")
        time.sleep(1)
    elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
        print("Lactose free selected")
        print(" ")
        time.sleep(1)
        for i in range(len(drinks)):
            if "lactosefree" in drinkrestrictions[i]:
                recommendeditems.append(drinks[i])
                recommendedingredients.append(drinkingredients[i])
        print("Generating random drink now...")
        time.sleep(1)
    else:
        print("No dietary restrictions/choices selected.")
        print(" ")
        print("Generating random drink now...")
        time.sleep(1)
        for i in range(len(drinks)):
            recommendeditems.append(drinks[i])
            recommendedingredients.append(drinkingredients[i])
    randomindex=random.randint(0,(len(recommendeditems)-1))
    generateditem = recommendeditems[randomindex]
    generateditemingredients=recommendedingredients[randomindex]
    print(" ")
    print("Suggested drink: " + generateditem)
    photoindex = drinks.index(generateditem)
    open_image(drinkphotolinks[photoindex])
    time.sleep(1)
    finalrecommendations.append(generateditem)
    finalingredients.append(generateditemingredients)


def itemrecommender(amountofitems):
    for i in range(amountofitems):
        print(" ")
        print("Would you like a salad(1), sandwich(2), soup(3), or drink(4)?")
        print(" ")
        try:
            menugroup=int(input("Please select a choice 1-4."))
        except:
            print("Please selected a number 1-4")
        if menugroup==1:
            saladselection()
        elif menugroup==2:
            sandwichselection()
        elif menugroup==3:
            soupselection()
        elif menugroup==4:
            drinkselection()
        else:
            print("Invalid choice")
            print(" ")
            print("Restaring recommending process...")
            itemrecommender(amountofitems)
    time.sleep(1)
    print(" ")
    print("Your final recommendations: ")
    for i in range(len(finalrecommendations)):
        print("-" + finalrecommendations[i])
        print("(" + finalingredients[i] + ")")


def entiremenurecommender():
    print("Hello! Welcome to the Eagle's Nest Cafe.")
    print(" ")
    time.sleep(1)
    print("We use a menu recommender to ensure the best experience!")
    time.sleep(1)
    print(" ")
    print("How many items will you be ordering today(enter numeric value)?")
    itemrecommender(int(input("Enter numeric value here:")))
    time.sleep(3)
    print(" ")
    print("Thank you for using the item recommender. Enjoy your food!")


#Main
entiremenurecommender()

#Photo Sources:
#Chicken Caeser Salad Photo: https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_auto,w_728,h_546/k%2FPhoto%2FRecipes%2F2024-04-chicken-caesar-salad%2Fchicken-caesar-salad-653
#Garden Salad Photo: https://www.missinthekitchen.com/wp-content/uploads/2020/03/Green-Salad-Recipe-Image-683x1024.jpg
#Caprese Salad Photo: https://www.thespruceeats.com/thmb/QZtRJibA70fH7B5XKodp_1HTS7k=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/caprese-salad-tomato-salad-2217097-hero-03-75a0b89b30aa4a52b10fe4fdd9abfeb5.jpg
#Chicken Noodle Soup Photo: https://www.bigbearswife.com/wp-content/uploads/2020/05/30-Minute-Pantry-Chicken-Noodle-Soup-3-731x1024.png
#Chili Photo: https://hips.hearstapps.com/hmg-prod/images/beef-chili-lead-6630087a9ab98.jpg?crop=0.9994794377928162xw:1xh;center,top&resize=1200:*
#Tomato Soup Photo: https://www.allrecipes.com/thmb/jbodaMY5KLc7g5gHmHMT2MUqjvE=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/277311spicy-fresh-tomato-soupFranceC4x3-56454ad082214f33960f62665fc8c169.jpg
#BLT Photo: https://dyvn6jpt1f0d3.cloudfront.net/wp-content/uploads/2023/10/14154227/BLT-for-recipe-1-6-980x551.jpeg
#Gluten Free Grilled Cheese Photo: https://www.allrecipes.com/thmb/CZ93z2oGv0n9ZsLp5yE2Lgb0Tyk=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/AR-238891-Grilled-Cheese-Sandwich-beauty-4x3-362f705972e64a948b7ec547f7b2a831.jpg
#Veggie Sandwich Photo: https://www.andiemitchell.com/wp-content/uploads/2019/01/best_veggie_sandwich_hummus_avocado-2.jpg
#Club Sandwich Photo: https://www.seriouseats.com/thmb/0nUt5iaqM54mdfbWRv6A8VrP_Yo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/20231204-SEA-TurkeyClub-FredHardy-03-e345fa83f2b4492d8c921d1dbd91a596.jpg
#Still Water Photo: https://sojo.net/sites/default/files/blog/shutterstock_65621872_0.jpg
#Sparkling Water Photo: https://www.nextlevelurgentcare.com/wp-content/uploads/elementor/thumbs/AdobeStock_233416704-scaled-q7kwpmr1z68b3zzupki2yr9ffad06ve4c0fyj6v5kw.jpeg
#Soda Photo: https://134532506.cdn6.editmysite.com/uploads/1/3/4/5/134532506/s549469990591119337_p28_i3_w900.jpeg?width=2400&optimize=medium
#Apple Juice Photo: https://parade.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_700/MjAwNjM4NjE1MDExNzMwODA4/is-apple-juice-good-for-you.webp
#Orange Juic Photo: https://images-prod.healthline.com/hlcmsresource/images/AN_images/orange-juice-1296x728-feature.jpg
#Strawberry Banana Smoothie Photo: https://www.simplyrecipes.com/thmb/YZRqiGDbKwgaw1ayN6LykaoieAA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Simply-Recipes-Strawberry-Banana-Smoothie-LEAD-2-RECIRC-40ae66e586a341d7951fa38f5659fac4.jpg
