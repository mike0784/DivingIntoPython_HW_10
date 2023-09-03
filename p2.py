from datetime import datetime
class animal:
    date_format = "%d/%m/%Y"
    def __init__(self, name: str, birth: str) -> None:
        self.name = name
        self.birth = birth
        pass

    def getName(self) -> str:
        return self.name
    
    def age(self) -> str:
        print(self.birth)
        date_obj = datetime.strptime(self.birth, '%d-%m-%Y')
        current_date = datetime.today()
        age = current_date - date_obj
        return f'Возраст: {age.days} дней'
    
    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

class animalFactory:
    def get_animal(self, type: str, name: str, birth: str, value: str):
        if type == "cat":
            return cat(name, birth, value)
        elif type == "fish":
            return fish(name, birth, value)
        elif type == "birds":
            return birds(name, birth, value)
        else:
            raise ValueError(format)


class cat(animal):
    def __init__(self, name: str, birth: str, breed: str) -> None:
        super().__init__(name, birth)
        self.breed = breed
    
    def __str__(self):
        return f'Порода кошки: {self.breed}'

class fish(animal):
    def __init__(self, name: str, birth: str, water: str) -> None:
        super().__init__(name, birth)
        self.water = water
    
    def __str__(self):
        return f'Рыба {self.water}'

class birds(animal):
    def __init__(self, name: str, birth: str, bird_species: str) -> None:
        super().__init__(name, birth)
        self.bird_species = bird_species
    
    def __str__(self):
        return f'Птица {self.bird_species}'


if __name__ == "__main__":
    factory = animalFactory()
    obj = factory.get_animal("cat", "Барсик", "12-04-2022", "Сфинкс")
    print(obj)
    print(obj.age())

    obj1 = factory.get_animal("cat", "Барсик", "12-04-2022", "Сфинкс")
    obj2 = factory.get_animal("fish", "Разящий", "04-04-2019", "пресноводный")
    obj3 = factory.get_animal("birds", "Карумба", "23-06-2010", "Водоплавающий")

    print(f'Объект 1: {obj1}, {obj1.age()}')
    print(f'Объект 2: {obj2}, {obj2.age()}')
    print(f'Объект 3: {obj3}, {obj3.age()}')