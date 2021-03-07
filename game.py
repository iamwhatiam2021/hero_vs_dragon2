import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
hero_hp = 50
dragon_hp = 100
hero_max_dmg = 20
dragon_max_dmg = 10

print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")

# add a While for an infinite block
# here goes the while:
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp = hero_hp - dragon_attack
     # here you need to update the hero hp, you need to subtract the damage that the dragon did
    # add code on this line

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    # add an if condition to check if the hero was killed by the dragon
    # here goes the if
    if hero_hp <=0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    # add code on this line
    dragon_hp= dragon_hp - hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    # add an if condition to check if the dragon was killed by the hero
    # here goes the if
    if dragon_hp <= 0:
        print("Our valiant hero has slain the dragon!")
        break

    input("Round over. Press any key")