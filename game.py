from elements import *
from great_hero import *
from activti import *
from location import *

def game():
    live = True
    while live:
        print("Посещать локацию можно один раз - исключение : сюжетное убийство ключевого персонажа")

        print(" Куда вы пойдете ? \n 1) Церковь \n 2) Полиция \n 3) Кладбище \n 4) Переулок темных сделок \n 5) перекресток для вызова демона  \n 6) Искать пророчества у ведьмы")
        lotions_one = int(input("Ввдите число "))        
        

        if lotions_one == 1:
            timple()
            if hero.health < 0:
                print("Игра оконченна")
                live = False

        if lotions_one == 2:
            police_ofice()
            if hero.health < 0:
                print("Игра оконченна")
                live = False
        
        if lotions_one == 6:
            iga()
            if hero.health < 0:
                print("Игра оконченна")
                live = False

        if lotions_one == 3:
            cemetery()
            if hero.health < 0:
                print("Игра оконченна")
                live = False

        if lotions_one == 4:
            secta()
            if hero.health < 0:
                print("Игра оконченна")
                live = False
    
        if lotions_one == 5:
            satana()
            if hero.health < 0:
                print("Игра оконченна")
                live = False

    