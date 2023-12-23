import random
list = ["well","well","witchut"]
def interlayer(char, destination, time = 0):
    if time != 0:
        print("прошло ",time," часов")
        print()
    if "poisoned" in char.traits:
        char.health = char.health - time* 2
        print("из за отравления, вы чувствуюте себя хуже")
        print()
    char.hunger = char.hunger-time*2
    char.shiza = char.shiza+ time*2
    if char.shiza >= 100:
        print("вы сошли с ума")
        dead()
    if char.hunger <= 0:
        print("вы умерли от голода")
        dead()
    if char.health <= 0:
        print("вы умерли от потери здоровья")
        dead()
    print("сытость:",char.hunger,", шиза:",char.shiza,", здоровье:", char.health)
    match destination:
        case "road":
            road(char)
        case "well":
            well(char)
        case "witchut":
            witchut(char)



def dead():
    print("you are dead")


def road(char):
    print("вы идёте по дороге")
    print("1-поспать 8 часов, 2-идти дальше ")
    d = int(input())
    if d == 1:
        char.shiza = char.shiza-40
        char.hunger = char.hunger-20
        print("вы поспали и востановили рассудок, но вы сильнее хотите есть")
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

        print("никого нет, но есть два зелья")
        print("сколько вы хотите выпить?(0/1/2)")
        d2 = int(input())
        if d2 == 0:
            print("вы не взяли ничего и вернулись на дорогу")
            interlayer(char,"road",0)
        if d2 == 1:
            print("вы выпили что-то , на вкус как противоядие, и вернулись на дорогу")
            if "poisoned" in char.traits:
                char.traits.remove("poisoned")

            interlayer(char,"road",0)
        if d2 == 1 and i2 <1 :
            if i3 == 1:
                print("вы выпили что-то , на вкус как противоядие, и вернулись на дорогу")
            if i3 ==2:
                print("вы выпили что-то , на вкус как зелье лечения, и вернулись на дорогу")
                char.health = char.health + 20
            interlayer(char,"road",0)
        if d2 == 2:
            if i3 == 1:
                print("вы разбили два флакона и вернулись на дорогу")
            if i3 == 2:
                char.health = char.health + 20     
                char.traits.remove("poisoned")    
                print("вы что-то выпили и вернулись на дорогу")          
            interlayer(char,"road",0)
    elif d == 2:
        interlayer(char,"road",0)
