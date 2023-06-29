from elements import *
from great_hero import *
import random



def batle(boss, hero):
    print(boss.enter_boss())
    print(hero.enter_hero())


    while boss.health > 0:
        winner = True
        print("Ваше здоровье:",hero.health)
        print("Здоровье босса", boss.health)
        action = int(input("Выберите действие: 1) Атаковать 2) Бежать "))
        
        if action == 1:
            damage = boss.defense - hero.attack
            print(damage)
            if damage < 0:
                boss.health += damage

            damage_hero = hero.defense - boss.attack
            if damage_hero < 0:
                hero.health += damage_hero
            if hero.health <= 0:
                print("Вас убил", boss.name)
                break
        
        if action == 2:
            runner = random.randint(1, 2)
            if runner == 1:
                winner = False
                break
            else:
                damage_hero = hero.defense - boss.attack
                if damage_hero < 0:
                    hero.health += damage_hero


    if hero.health > 0 and winner == True:
        print("Вы победили босса ", boss.name)
        print(boss.help)
    elif winner == False:
        print("Вы трусливо бежали, но остались живы")
    


    
