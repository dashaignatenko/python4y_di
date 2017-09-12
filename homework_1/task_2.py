"""
Здравствуйте это пасека
Из чего она состоит:
1. собственно, класс пасеки, у которого есть аргумент "hives" - это
массив с ульями
2. классы пчёл - базовый класс Pchela и три класса, наследующих его св-ва
(Pchela_rabochaja, Trutenj, Pchela_matka)
3. в каждый объект класса улей поселяется одна пчелиная семья - от 1 до 9 тысяч
трутней и какое-то количество рабочих пчел, зависящее от количества трутней
для класса ульев есть функция: посчитать, сколько мёду собирается за сеозон -
вот тут используется полиморфизм: программа как бы рассматривает каждую пчелу
из улья, и если пчела оказывается рабочей (а не маткой и трутнем), то считается,
что она приносит в улей какое-то количество мёда (random.uniform(0.01,0.03) * b.daysalive())
b.daysalive() - количество дней жизни пчелы, которое определяется в базовом класе
одинаково для всех пчёл
4. класс мед - количество меда, собранного с пасеки за сезон
"""
import random

class Paseka:
    def __init__(self, hives = []):
        self.hives = hives

class Pchela:
    def __init__(self):
        self.days_alive = random.randint(30,50)
    def daysalive(self):
        return self.days_alive
    def makes_honey(self):
        return True

class Pchela_rabochaja(Pchela):
    def __init__(self):
        super().__init__()
    def makes_honey(self):
        return True

class Trutenj(Pchela):
    def __init__(self):
        super().__init__()
    def makes_honey(self):
        return False

class Pchela_matka(Pchela):
    def __init__(self):
        super().__init__()
    def makes_honey(self):
        return False
    
class Ulej():
    def __init__(self):
        self.bees = [Pchela_matka()]
        self.bees += [Trutenj()] * random.randint(1,9) #тысяч трутней
        self.bees += [Pchela_rabochaja()] * len(self.bees) * random.randint(2,11)
    def honey_season(self):
        honey_kg = 0
        for b in self.bees:
            if b.makes_honey:
                honey_kg += random.uniform(0.01,0.03) * b.daysalive()
        return honey_kg

class Honey:
    def __init__(self, paseka):
        self.paseka = paseka
    def count_honey(self):
        self.honey = 0
        for h in self.paseka.hives:
            self.honey += h.honey_season()
        return '%s kg of honey were collected' % (self.honey)

paseka = Paseka()
paseka.hives = [Ulej()] * 3
print(Honey(paseka).count_honey())

