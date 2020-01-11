class Person:
    inventory = []
    gameinventory = []
    classs = ""
    cash = 0


person = Person()

items = { "normal dagger" : 20, "normal sword" : 50, "mace" : 45, "morgenstern" : 25}

print(", ".join(["[%s - %d]"%(k,v) for (k, v) in items.items()]))


blacksmithinv = ["[normal dagger - 20]","[normal sword - 50]"]
gameblacksmithinv = [[20,[20,15]],[50,[10,7]]]

def begining():
    while True:
        print("Hello brave adventurer, are you here to save the land of the phoenix?")
        print("[Yes] [No]")
        yesorno = input("")
        if yesorno == "Yes":
            break

def begining2():
    print("thank god weve been searching for such a long time")
    while True:
        print("So, whats your name?")
        name = input()
        print("Ah, so its the",name+"?")
        print("[Yes] [No]")
        yesorno = input()
        if yesorno == "Yes":
            break
    print("What class are you?")
    print("[swordwielder] [archer] [thief]")
    classs = input("")
    while True:
        if classs == "swordwielder" or classs == "archer"  or classs == "thief":
            return classs
        print("could you repeat that, I didint understand you")
        classs = input()

def item1(plswork):
    if plswork == "archer":
        print("You received a bow!")
        inventory.append("beginner bow")
        gameinventory.append([5,5])
        print("with the archer class you will be abel to damage enemies from afar")
    if plswork == "swordwielder":
        print("You received a sword!")
        inventory.append("begginer sword")
        gameinventory.append([10,5])
        print("with the swordwielder class you will be able to deal massive damage")
    if plswork == "thief":
        print("You received a dagger!")
        inventory.append("beginner dagger")
        gameinventory.append([5,5])
        print("with the thief class you will be able to pickpocket people, but deal little damage")
    print("now go save the land of the phoenix")
def togo1(inventory,classs):
    print("Where would you like to go?")
    print("[The city] [The forest]")
    where = input("")
    if where == "The city":
        Hamburg(classs,inventory,cash,blacksmithinv,gameblacksmithinv)

def blacksmithofhamburg(money,blacksmithinv,gameblacksmithinv):
    print("[Buy] [Sell] [leave]")
    print('please enter the number of the item you want to buy or leave')
    where = input('')
    if where == "Buy":
        print(blacksmithinv,"[leave]")
        where = input('')
    if where == "leave":
        Hamburg(classs,inventory)
    if where == "Sell":
        print("this isnt available yet")
        blacksmithofhamburg(money,blacksmithinv,gameblacksmithinv)
    where = int(where)
    if where >= len(blacksmithinv):
        print("so you want to buy",blacksmithinv[where+"?"])
        print("[Yes] [No]")
        where1 = input('')
        if where1 == "Yes":
            if money >= gameblacksmithinv[where][0]:
                print("you have sucesfully bought",blacksmithinv[where])
                cash = cash - gameblacksmithinv[where][0]
                inventory.append(blacksmithinv[where])
                gameinventory.append(gameblacksmithinv[where][1])
            else:
                print("you don't have enough money")
        blacksmithofhamburg(money,blacksmithinv,gameblacksmithinv)



def Hamburg(classs,inventory,money,blacksmithinv,gameblacksmithinv):
    print("you've entered your home town hamburg.")
    print('[Blacksmith] [Armor maker] [potions] [fletcher] [leave]')
    where = input('')
    if where == "Blacksmith":
        blacksmithofhamburg(money,blacksmithinv,gameblacksmithinv)

        
            



def game():
    begining()
    classs = begining2()
    item1(classs)
    togo1(inventory,classs)
game()