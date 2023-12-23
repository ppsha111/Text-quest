import random
list = ["well","OldLady",2]
def interlayer(char, destination, time = 0):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if time != 0:
        print("прошло ",time," часов")
        print()
    if "poisoned" in char.traits:
        char.health = char.health - time* 2
        print("из за отравления, вы чувствуюте себя хуже")
    if "plauge" in char.traits:
        char.health = char.health - time* 3
        print("из за болезни, вы чувствуюте себя хуже")
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
    print("сытость:",char.hunger,", шиза: ",char.shiza,", здоровье: ", char.health,"деньги: ",char.money)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    match destination:
        case "road":
            road(char)
        case "well":
            well(char)
        case "witchut":
            witchut(char)
        case "OldLady":
            OldLady(char)
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
        char.shiza = char.shiza-30
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
                print("у вас получилось выломать дверь, вы очутились рядом с хижиной ведьмы")
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



def OldLady(char):
    i = random.choice(["witch","plauge","doctor","doctor","doctor"])
    if i == "witch" and "stole from the witch" in char.traits:
        print("она на тебя набрасывается со словами: ты украл мои зелья")
        interlayer(char,"basement",random.randint(6,9))
        char.traits.remove("stole from witch")
    if i == "witch":
        print("привет, хочешь я тебя зельем угощу")
        print("1- да, 2- нет")
        d1 = int(input())
        if d1 == 1:     
            i = random.randint(1,3)
            match i:
                case 1:
                    print("вы выпили зелье похожее на яд")
                    char.traits.add("poisoned")
                case 2:
                    print("вы выпили зелье похожее на зелье лечения")
                    char.health = char.health+20    
                case 3:
                    print("вы выпили зелье похожее на противоядие")   
                    if "poisoned" in char.traits:
                        char.traits.remove("poisoned")
        print("вы развернулись, но старуха испарилась")
        interlayer(char,"road",0)
    if i == "plauge":
        print("вы втретили прокажённую")
        print("1 - пройти мимо, 2 - обокрасть")
        d1 = int(input())
        if d1 == 1:
            if random.randint(1,10)<2:
                char.traits.add("plauge")
                print("вам стало хуже")
            print("вы возвращаетесь на дорогу")
        if d1 == 2:
            if random.randint(1,3)<2:
                char.traits.add("plauge")
                print("вам стало хуже")
            char.money = char.money+random.randint(20,100)
            print("вы украли немного денег и вернулись на дорогу")
        interlayer(char,"road",0)
    if i == "doctor":
        print("вы видете человека в маске")
        print("он говорит: привет, я чумной доктор, если хочешь вылечиться, заплати мне 100 монет")
        print("1 - попросить лечния, 2 - ограбить, 3- пройти мимо ")
        d1 = int(input())
        match d1:
            case 1:
                if char.money>99:
                    char.health = char.health+ 50
                    if "plauge" in char.traits:
                        char.traits.remove("plauge")
                    if "poisoned" in char.traits:
                        char.traits.remove("poisoned")
                    char.money = char.money-100
                    print("вам стало гораздо лучше, поэтому вы возвращаетсь на дорогу")
                if char.money <100:
                    print("вы не можете себе это позволить, поэтому возвращаетсь на дорогу")
                interlayer(char,"road",0)
            case 2:
                if random.randint(1,100)>30:
                    char.money = char.money+random.randint(30,150)
                    print("вы украли немног денег и быстро вернулись на дорогу")
                    interlayer(char,"road",0)
                print("вас поймали и избили, но вы смогли сбежать")
                char.traits.add("wanted")
                char.health = char.health - random.randint(10,60)
                interlayer(char,"road",0)
            case 3:
                print("вы вернулись на дорогу")
                interlayer(char,"road",0)                

