import random
list = ["well","well","witchut"]
def interlayer(char, destination, time = 0):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if time != 0:
        print("прошло ",time," часов")
        print()
    if "poisoned" in char.traits:
        char.health = char.health - time* 2
        print("из за отравления, вы чувствуюте себя хуже")
    char.hunger = char.hunger-time*2
    char.shiza = char.shiza+ time*2
    if char.shiza >= 100:
        print("вы сошли с ума")
        dead()
    elif char.hunger <= 0:
        print("вы умерли от голода")
        dead()
    elif char.health <= 0:
        print("вы умерли от потери здоровья")
        dead()
    print("сытость:",char.hunger,", шиза:",char.shiza,", здоровье:", char.health)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    match destination:
        case "road":
            road(char)
        case "well":
            well(char)
        case "witchut":
            witchut(char)
        case "basement":
            basement(char)



def dead():
    print("you are dead")
    exit()


def road(char):
    print("вы идёте по дороге")
    print()
    print("1-поспать 8 часов, 2-идти дальше ")
    d = int(input())
    if d == 1:
        char.shiza = char.shiza-20
        print("вы поспали и востановили рассудок, но вы сильнее хотите есть")
        interlayer(char,"road",random.randint(7,8))       
    interlayer(char,random.choice(list),random.randint(1,5))



def well(char):
    print("вы встречаете колодец")
    print("1 - попить, 2 - вернутся на дорогу:")
    d = int(input())
    i = random.randint(1,3)
    if d == 1:
        if i == 1:
            char.hunger = char.hunger - 30
            print("кажется, что колодец был отравлен")
            char.traits.add("poisoned")
        elif i >1:
            char.hunger = char.hunger + 40
            print("вы попили и чувствуете насыщение")
        interlayer(char,"road",0)
    elif d == 2:
        interlayer(char,"road",0)
    
def witchut(char):
    print("вы встречаете хижину ведьмы")
    print("1 - войти, 2 - вернутся на дорогу:")
    d = int(input())
    i = random.randint(1,2)
    i2 = random.randint(1,5)
    i3 = random.randint(1,2)
    if d == 1:
        print("вы входите в хижину")
        if i != 1:
            print("никого нет, но есть два зелья")
            print("сколько вы хотите выпить?(0/1/2)")
            d2 = int(input())
            if d2 == 0:
                print("вы не взяли ничего и вернулись на дорогу")
                interlayer(char,"road",0)
            if d2 == 1 :
                char.traits.add("stole from the witch")
                if i3 == 1:
                    print("вы выпили что-то , на вкус как противоядие, и вернулись на дорогу")
                    if "poisoned" in char.traits:
                        char.traits.remove("poisoned")
                elif i3 == 2:
                    print("вы выпили что-то , на вкус как зелье лечения, и вернулись на дорогу")
                    char.health = char.health + 20
                interlayer(char,"road",0)
            if d2 == 2:
                char.traits.add("stole from the witch")
                if i3 == 1:
                    print("вы разбили два флакона и вернулись на дорогу")
                if i3 == 2:
                    char.health = char.health + 20     
                    if "poisoned" in char.traits:
                        char.traits.remove("poisoned")  
                interlayer(char,"road",0)
        elif i == 1:
            print("в хижене была ведьма")
            print("ведьма на вас напрыгнула")
            interlayer(char,"basement",random.randint(5,10))                 
    elif d == 2:
        interlayer(char,"road",0)


def basement(char):
    print("ты в подвале")
    print("1 - попытаться выломать дверь, 2 - спать, 3 - обыскать")
    d = int(input())
    match d:
        case 1:
            if random.randint(1,3) > 2:
                print("у вас получилось выломать дверь")
                interlayer(char,"witchut",0)    
            else:
                char.health = char.health - 10
                print("вы немного повредили руку")
                interlayer(char,"basement",random.randint(1,8))            
        case 2:
            print("вы решили спать")
            char.shiza = char.shiza - 30     
            interlayer(char,"basement",random.randint(7,8))    
        case 3:
            if random.randint(1,7) > 1:
                print("вы обыскали подвал, но ничего не нашли")
                interlayer(char,"basement",random.randint(1,3)) 
            else:
                print("вы нашли человеческое мясо")
                print("1 - съесть, 2 - не есть") 
                d2 =int(input())
                if d2 == 1:
                    char.shiza = char.shiza + 30
                    char.hunger = char.hunger + 40
                interlayer(char,"basement",random.randint(1,3))                 



# def OldLady(char):
#     i = random.choice("witch","plauge","doctor","doctor","doctor")
#     if i == "witch" and "stole from the witch" in char.traits:

