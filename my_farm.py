class Animal():

    animals_count = 0
    sum_weight = 0
    item_dict = {}
    item_list = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.__class__.sum_weight += self.weight
        self.__class__.item_dict[self.name] = self.weight
        Animal.animals_count += 1
        Animal.item_dict[self.name] = self.weight
        Animal.item_list.append(self.__class__.item_dict)
        Animal.sum_weight += self.weight

    def feed_the_animal(self, name):
        print(self.name + ' накормлен.')

    def animals_weight():
        print(f'Общий вес всех животных на ферме {Animal.sum_weight}.' 
                f'\n Общий вес гусей - {Goose.sum_weight} кг.'
                f'\n Общий вес коров - {Cow.sum_weight} кг.'
                f'\n Общий вес овец - {Sheep.sum_weight} кг.'
                f'\n Общий вес куриц - {Chicken.sum_weight} кг.'
                f'\n Общий вес уток - {Duck.sum_weight} кг.'
                f'\n Общий вес коз - {Goat.sum_weight} кг.')
        
def max_weight():
    b = Animal.item_dict.items()
    c = list(b)
    s = sorted(Animal.item_dict, key=Animal.item_dict.get, reverse=True)
    start_value = 0
    result_dict = {}
    for k, v in c:
        if s[0] in k:
            print(f'Самое тяжелое животное {k} весит {v} кг.')

class Cow(Animal):

    voice = 'Mooo'
    sum_weight = 0
    item_dict = {}
    
    def milk_the_animal(self):
        print(self.name + ' подоена.')

class Sheep(Animal):

    voice = 'Bee'
    sum_weight = 0
    item_dict = {}

    def trim_the_animal(self):
        print('Овечка ' + self.name + ' подстрижена.')

class Goose(Animal):

    voice = 'Ga-ga-ga'
    sum_weight = 0
    item_dict = {}

    def collect_eggs(self):
        print('У ' + self.name + ' яйца собраны.')

class Chicken(Goose):
        
    voice = 'Glo'
    sum_weight = 0
    item_dict = {}

class Duck(Goose):

    voice = 'Krya-krya'
    sum_weight = 0
    item_dict = {}

class Goat(Cow):

    voice = 'Be-ee'
    sum_weight = 0
    item_dict = {}

goose_1 = Goose('Серый', 10)
goose_2 = Goose('Белый', 9)
cow = Cow('Мурка', 210)
sheep_1 = Sheep('Барашек', 50)
sheep_2 = Sheep('Кудрявый', 60)
chicken_1 = Chicken('Ко-Ко', 5)
chicken_2 = Chicken('Кукареку', 6)
goat_1 = Goat('Рога', 15)
goat_2 = Goat('Копыта', 14)
duck = Duck('Кряква', 7)

Animal.animals_weight()
max_weight()