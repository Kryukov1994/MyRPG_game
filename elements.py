

class Hero:
    def __init__(self, name, health , attack, defense) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def enter_hero(self):
        print(f"Ваш герой: {self.name} \n здоровье: {self.health} \n Атака: {self.attack} \n Броня: {self.defense} ")

class Boss:
    def __init__(self, name, health, attack, defense, help) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.help = help
    
    def enter_boss(self):
        print(f"Враг: {self.name} \n здоровье: {self.health} \n Атака: {self.attack} \n Броня: {self.defense} ")


class Cannibal(Boss):
    def __init__(self) -> None:
        super().__init__( "Людоед ", 100, 50, 20, "1 слово заклинания для освобождния жены у демона: ночь")

class Demonl(Boss):
    def __init__(self) -> None:
        super().__init__( "Демон ", 500, 70 , 40, "Оке..... Твоя жана свободна, вы спали мир")

class With(Boss):
    def __init__(self) -> None:
        super().__init__( "Старая ведьма ", 100, 100, 20, "2 слово заклинания для освобождния жены у демона: темна")

class Outlaw(Boss):
    def __init__(self) -> None:
        super().__init__( "Разбойник ", 50, 30, 10)

class Sectarian(Boss):
    def __init__(self) -> None:
        super().__init__( "Сектант ", 200, 50, 30, "3 слово заклинания для освобождния жены у демона: жизнь")

class Pastor(Boss):
    def __init__(self) -> None:
        super().__init__( "Пастырь ", 300, 45, 30, "За убийство князя церки тебя ждут вечные муки")

class Police(Boss):
    def __init__(self) -> None:
        super().__init__( "Начальник полиции ", 100, 35, 10, "4 слово заклинания для освобождния жены у демона: коротка" )