#Olivia Kulinski
#Ideal dog breed
#2.27.2025

#Init
from PIL import Image
import requests
from io import BytesIO
import random
import time

dogImages=["https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg","https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg","https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg","https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg","https://cdn2.thedogapi.com/images/36TXlWMDf.jpg","https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg","https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg","https://cdn2.thedogapi.com/images/GhtSdrW29.jpg","https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg","https://cdn2.thedogapi.com/images/uISezUGDV.jpg","https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png","https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg","https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg","https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg","https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg","https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg","https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg","https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg","https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg","https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg","https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg","https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg","https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg","https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg","https://cdn2.thedogapi.com/images/HJAFgxcNQ_1280.jpg","https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg","https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg","https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg","https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg","https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg","https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg","https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg","https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg","https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg","https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg","https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg","https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg","https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg","https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg","https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg","https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg","https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg","https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg","https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg","https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg","https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg","https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg","https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg","https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg","https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg","https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg","https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg","https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg","https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg","https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg","https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg","https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg","https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg","https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg","https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg","https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg","https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg","https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg","https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg","https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png","https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg","https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg","https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg","https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg","https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg","https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg","https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg","https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg","https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg","https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg","https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg","https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg","https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg","https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg","https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg","https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg","https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg","https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg","https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg","https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg","https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg","https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg","https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg","https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg","https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg","https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg","https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg","https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg","https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg","https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg","https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg","https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg","https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg","https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg","https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"]
dogBreeds=["Affenpinscher","AfghanHound","AiredaleTerrier","AkbashDog","Akita","AlapahaBlueBloodBulldog","AlaskanHusky","AlaskanMalamute","AmericanEskimoDog","AmericanFoxhound","AmericanPitBullTerrier","AmericanWaterSpaniel","AnatolianShepherdDog","AustralianKelpie","AustralianShepherd","Azawakh","Basenji","BassetBleudeGascogne","Beagle","Beauceron","BedlingtonTerrier","BelgianMalinois","BelgianTervuren","BerneseMountainDog","BlackandTanCoonhound","Bloodhound","BluetickCoonhound","Boerboel","BorderTerrier","BostonTerrier","BouvierdesFlandres","Boxer","BoykinSpaniel","BraccoItaliano","Briard","Brittany","Bullmastiff","CairnTerrier","CaneCorso","CardiganWelshCorgi","CatahoulaLeopardDog","CaucasianShepherd(Ovcharka)","CavalierKingCharlesSpaniel","ChineseCrested","Chinook","ChowChow","ClumberSpaniel","CockerSpaniel(American)","CotondeTulear","Dalmatian","DogoArgentino","EnglishShepherd","EnglishSpringerSpaniel","Eurasier","FieldSpaniel","FinnishLapphund","GermanPinscher","GermanShepherdDog","GermanShorthairedPointer","GiantSchnauzer","GlenofImaalTerrier","GoldenRetriever","GordonSetter","GreatDane","GreatPyrenees","Greyhound","Harrier","Havanese","IrishSetter","IrishWolfhound","ItalianGreyhound","JapaneseChin","Keeshond","Komondor","Kuvasz","LabradorRetriever","LagottoRomagnolo","Leonberger","LhasaApso","Maltese","MiniatureSchnauzer","Newfoundland","NorfolkTerrier","Papillon","PembrokeWelshCorgi","PharaohHound","Plott","Pug","RedboneCoonhound","RhodesianRidgeback","Rottweiler","Samoyed","Schipperke","ScottishDeerhound","ShihTzu","SilkyTerrier","SoftCoatedWheatenTerrier","SpanishWaterDog","Vizsla","Weimaraner"]
dogBreeds2 = [dogs.lower() for dogs in dogBreeds]
dogWeights=[6,50,40,90,65,55,38,65,20,65,30,25,80,31,35,33,22,35,20,80,17,40,40,65,65,80,45,110,12,10,70,50,25,55,70,30,100,13,88,25,50,80,13,10,50,40,55,20,9,50,80,44,35,40,35,33,25,50,45,65,32,55,45,110,85,50,40,7,35,105,7,4,35,80,70,55,24,120,12,4,11,100,11,3,25,40,40,14,45,75,75,50,10,70,9,8,30,30,50,55]
bredFor = ["Small rodent hunting, lapdog"," Coursing and hunting","Badger, otter hunting"," Sheep guarding"," Hunting bears"," Guarding"," Sled pulling"," Hauling heavy freight, Sled pulling"," Circus performer"," Fox hunting, scent hound"," Fighting"," Bird flushing and retrieving"," Livestock herding"," Farm dog, Cattle herding"," Sheep herding"," Livestock guardian, hunting"," Hunting"," Hunting on foot."," Rabbit, hare hunting"," Boar herding, hunting, guarding"," Killing rat, badger, other vermin"," Stock herding"," Guarding, Drafting, Police work."," Draft work"," Hunting raccoons, night hunting"," Trailing"," Hunting with a superior sense of smell."," Guarding the homestead, farm work."," Fox bolting, ratting"," Ratting, Companionship"," Cattle herding"," Bull-baiting, guardian"," Turkey retrieving"," Versatile gun dog"," Herding, guarding sheep"," Pointing, retrieving"," Estate guardian"," Bolting of otter, foxes, other vermin"," Companion, guard dog, and hunter"," Cattle droving"," Driving livestock"," Guard dogs, defending sheep from predators, mainly wolves, jackals and bears"," Flushing small birds, companion"," Ratting, lapdog, curio"," Sled pulling"," Guardian, cart pulling, hunting"," Bird flushing, retrieving"," Hunting the American woodcock"," Accompanying ladies on long sea voyages, ratters onboard ship."," Carriage dog - trot alongside carriages to protect the occupants from banditry or other interference"," Big-game hunting"," Herding & guarding livestock, farm watch dog"," Bird flushing, retrieving"," Companionship"," Bird flushing, retrieving"," Herding reindeer"," Watchdog, Hunting vermin on the farm."," Herding, Guard dog"," General hunting"," Herding, guarding"," Rid the home and farm of vermin, and hunt badger and fox"," Retrieving"," Find and point gamebirds"," Hunting & holding boars, Guardian"," Sheep guardian"," Coursing hares"," Hunting hares by trailing them"," Companionship"," Bird setting, retrieving"," Coursing wolves, elk"," Lapdog"," Lapdog"," Barge watchdog"," Sheep guardian"," Guardian, hunting large game"," Water retrieving"," Water retrieval dog in the marshes of Romagna"," Guardian, appearance."," Guarding inside the home, companion"," Lapdog"," Ratting"," All purpose water dog, fishing aid"," Ratting, fox bolting"," Lapdog"," Driving stock to market in northern Wales"," Hunting rabbits"," Hunting big-game like Boar."," Lapdog"," Hunting raccoon, deer, bear, and cougar."," Big game hunting, guarding"," Cattle drover, guardian, draft"," Herding reindeer, guardian, draft"," Barge watchdog"," Coursing deer"," Lapdog"," Small vermin hunting, companionship"," Vermin hunting, guarding, all-around farm helper"," Herding flocks of sheep and goats from one pasture to another"," Pointing and trailing"," Large game trailing and versatile gundog"]
temperment=["Stubborn,Curious,Playful,Adventurous,Active,Fun-loving","Aloof,Clownish,Dignified,Independent,Happy","Outgoing,Friendly,Alert,Confident,Intelligent,Courageous","Loyal,Independent,Intelligent,Brave","Docile,Alert,Responsive,Dignified,Composed,Friendly,Receptive,Faithful,Courageous","Loving,Protective,Trainable,Dutiful,Responsible","Friendly,Energetic,Loyal,Gentle,Confident","Friendly,Affectionate,Devoted,Loyal,Dignified,Playful","Friendly,Alert,Reserved,Intelligent,Protective","Kind,Sweet-Tempered,Loyal,Independent,Intelligent,Loving","StrongWilled,Stubborn,Friendly,Clownish,Affectionate,Loyal,Obedient,Intelligent,Courageous","Friendly,Energetic,Obedient,Intelligent,Protective,Trainable","Steady,Bold,Independent,Confident,Intelligent,Proud","Friendly,Energetic,Alert,Loyal,Intelligent,Eager","Good-natured,Affectionate,Intelligent,Active,Protective","Aloof,Affectionate,Attentive,Rugged,Fierce,Refined","Affectionate,Energetic,Alert,Curious,Playful,Intelligent","Affectionate,Lively,Agile,Curious,Happy,Active","Amiable,EvenTempered,Excitable,Determined,Gentle,Intelligent","Fearless,Friendly,Intelligent,Protective,Calm","Affectionate,Spirited,Intelligent,Good-tempered","Watchful,Alert,Stubborn,Friendly,Confident,Hard-working,Active,Protective","Energetic,Alert,Loyal,Intelligent,Attentive,Protective","Affectionate,Loyal,Intelligent,Faithful","Easygoing,Gentle,Adaptable,Trusting,EvenTempered,Lovable","Stubborn,Affectionate,Gentle,EvenTempered","Friendly,Intelligent,Active","Obedient,Confident,Intelligent,Dominant,Territorial","Fearless,Affectionate,Alert,Obedient,Intelligent,EvenTempered","Friendly,Lively,Intelligent","Protective,Loyal,Gentle,Intelligent,Familial,Rational","Devoted,Fearless,Friendly,Cheerful,Energetic,Loyal,Playful,Confident,Intelligent,Bright,Brave,Calm","Friendly,Energetic,Companionable,Intelligent,Eager,Trainable","Stubborn,Affectionate,Loyal,Playful,Companionable,Trainable","Fearless,Loyal,Obedient,Intelligent,Faithful,Protective","Agile,Adaptable,Quick,Intelligent,Attentive,Happy","Docile,Reliable,Devoted,Alert,Loyal,Reserved,Loving,Protective,Powerful,Calm,Courageous","Hardy,Fearless,Assertive,Gay,Intelligent,Active","Trainable,Reserved,Stable,Quiet,EvenTempered,Calm","Affectionate,Devoted,Alert,Companionable,Intelligent,Active","Energetic,Inquisitive,Independent,Gentle,Intelligent,Loving","Alert,Quick,Dominant,Powerful,Calm,Strong","Fearless,Affectionate,Sociable,Patient,Playful,Adaptable","Affectionate,Sweet-Tempered,Lively,Alert,Playful,Happy","Friendly,Alert,Dignified,Intelligent,Calm","Aloof,Loyal,Independent,Quiet","Affectionate,Loyal,Dignified,Gentle,Calm,Great-hearted","Outgoing,Sociable,Trusting,Joyful,EvenTempered,Merry","Affectionate,Lively,Playful,Intelligent,Trainable,Vocal","Outgoing,Friendly,Energetic,Playful,Sensitive,Intelligent,Active","Friendly,Affectionate,Cheerful,Loyal,Tolerant,Protective","Kind,Energetic,Independent,Adaptable,Intelligent,Bossy","Affectionate,Cheerful,Alert,Intelligent,Attentive,Active","Alert,Reserved,Intelligent,EvenTempered,Watchful,Calm","Docile,Cautious,Sociable,Sensitive,Adaptable,Familial","Friendly,Keen,Faithful,Calm,Courageous","Spirited,Lively,Intelligent,Loving,EvenTempered,Familial","Alert,Loyal,Obedient,Curious,Confident,Intelligent,Watchful,Courageous","Boisterous,Bold,Affectionate,Intelligent,Cooperative,Trainable","StrongWilled,Kind,Loyal,Intelligent,Dominant,Powerful","Spirited,Agile,Loyal,Gentle,Active,Courageous","Intelligent,Kind,Reliable,Friendly,Trustworthy,Confident","Fearless,Alert,Loyal,Confident,Gay,Eager","Friendly,Devoted,Reserved,Gentle,Confident,Loving","StrongWilled,Fearless,Affectionate,Patient,Gentle,Confident","Affectionate,Athletic,Gentle,Intelligent,Quiet,EvenTempered","Outgoing,Friendly,Cheerful,Sweet-Tempered,Tolerant,Active","Affectionate,Responsive,Playful,Companionable,Gentle,Intelligent","Affectionate,Energetic,Lively,Independent,Playful,Companionable","Sweet-Tempered,Loyal,Dignified,Patient,Thoughtful,Generous","Mischievous,Affectionate,Agile,Athletic,Companionable,Intelligent","Alert,Loyal,Independent,Intelligent,Loving,Cat-like","Agile,Obedient,Playful,Quick,Sturdy,Bright","Steady,Fearless,Affectionate,Independent,Gentle,Calm","Clownish,Loyal,Patient,Independent,Intelligent,Protective","Kind,Outgoing,Agile,Gentle,Intelligent,Trusting,EvenTempered","Keen,Loyal,Companionable,Loving,Active,Trainable","Obedient,Fearless,Loyal,Companionable,Adaptable,Loving","Steady,Fearless,Friendly,Devoted,Assertive,Spirited,Energetic,Lively,Alert,Obedient,Playful,Intelligent","Playful,Docile,Fearless,Affectionate,Sweet-Tempered,Lively,Responsive,Easygoing,Gentle,Intelligent,Active","Fearless,Friendly,Spirited,Alert,Obedient,Intelligent","Sweet-Tempered,Gentle,Trainable","Self-confidence,Fearless,Spirited,Companionable,Happy,Lovable","Hardy,Friendly,Energetic,Alert,Intelligent,Happy","Tenacious,Outgoing,Friendly,Bold,Playful,Protective","Affectionate,Sociable,Playful,Intelligent,Active,Trainable","Bold,Alert,Loyal,Intelligent","Docile,Clever,Charming,Stubborn,Sociable,Playful,Quiet,Attentive","Affectionate,Energetic,Independent,Companionable,Familial,Unflappable","StrongWilled,Mischievous,Loyal,Dignified,Sensitive,Intelligent","Steady,Good-natured,Fearless,Devoted,Alert,Obedient,Confident,Self-assured,Calm,Courageous","Stubborn,Friendly,Sociable,Lively,Alert,Playful","Fearless,Agile,Curious,Independent,Confident,Faithful","Docile,Friendly,Dignified,Gentle","Clever,Spunky,Outgoing,Friendly,Affectionate,Lively,Alert,Loyal,Independent,Playful,Gentle,Intelligent,Happy,Active,Courageous","Friendly,Responsive,Inquisitive,Alert,Quick,Joyful","Affectionate,Spirited,Energetic,Playful,Intelligent,Faithful","Trainable,Diligent,Affectionate,Loyal,Athletic,Intelligent","Affectionate,Energetic,Loyal,Gentle,Quiet","Steady,Aloof,Stubborn,Energetic,Alert,Intelligent,Powerful,Fast"]
filteredList=[]
filteredList2=[]
recommendedDogs=[]


#Functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def randdog():
    return(filteredList[random.randint(0,(len(filteredList) -1))])

def getDogSize():
    print("""Our dog sizes include:
    1). Tiny less than 11 pounds
    2). Small 11-25 pounds
    3). Medium 26 - 60
    4). Large over 60 pounds""")
    Dogsize = int(input("What size dog are you looking for? Choose a number 1-4"))
    if Dogsize == 1:
        for i in range(len(dogWeights)):
            if dogWeights[i] < 11:
                filteredList.append(dogBreeds[i])
    elif Dogsize == 2:
        for i in range(len(dogWeights)):
            if  dogWeights[i] >= 11 and dogWeights[i] <= 25:
                filteredList.append(dogBreeds[i])
    elif Dogsize == 3:
        for i in range(len(dogWeights)):
            if dogWeights[i] >= 26 and dogWeights[i] <= 60:
                filteredList.append(dogBreeds[i])
    elif Dogsize == 4:
        for i in range(len(dogWeights)):
            if dogWeights[i] > 60:
                filteredList.append(dogBreeds[i])
    randomDog = randdog()
    print("Your ideal dogs is: " + randomDog)
    recommendedDogs.append(randomDog)


def dogbreed():
    breedChoice = input("What dog breed are you looking for?: ")
    if breedChoice in dogBreeds2:
        breedChoice = breedChoice.lower()
        breedChoice = breedChoice.replace(" ", "")
        index = 0
        for i in range(len(dogBreeds2)):
            if i != breedChoice:
                index = dogBreeds2.index(breedChoice)

        print(dogBreeds2[index])
        print(temperment[index])
        open_image(dogImages[index])
    else:
        print("Please enter a valid dog breed!")
def bredfor():
    choice = input("What purpose are you looking for in your dog? ")
    choice = choice.lower()
    for i in range(len(bredFor)):
        if choice in bredFor[i].lower():
            filteredList2.append(dogBreeds[i])
    recdog = filteredList2[random.randint(0,(len(filteredList2) -1))]
    recommendedDogs.append(recdog)

def recommendation(amountOfdogs):
    while True:
        print("""What are you looking for in our program?
        1. Finding desired amount of dogs based off size preferences
        2. Finding images and traits of chosen dogs
        3. Finding dogs based off specified purpose
        4. Quit""")
        userchoice = int(input("Pick your option: 1-4"))
        if userchoice == 1:
            for i in range(amountOfdogs):
                print("Choose the size of the dog you want for each dog")
                time.sleep(1)
                getDogSize()
            print("Your recommended dogs were... ")
            time.sleep(2)
            print(recommendedDogs)
            time.sleep(3)
        elif userchoice == 2:
            for i in range(amountOfdogs):
                dogbreed()
        elif userchoice == 3:
            for i in range(amountOfdogs):
                bredfor()
            print("Your recommended dogs were... ")
            time.sleep(2)
            print(recommendedDogs)
            time.sleep(3)
        elif userchoice == 4:
            print("Okay! Thanks for using our simulator!")
            break

print("Welcome to our Ideal Dog Breed Simulator!!")
print("Our simulator aims to find the perfect dog, just for YOU!!")
time.sleep(2)
recommendation(2)
