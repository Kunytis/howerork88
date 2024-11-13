class AgeError(Exception):
    def __init__(self, mesage):
        super().__init__(mesage)


class Human
    def __init__(self, name):
        self.name = name
        self.age = None

    def get_age(self, age):
        if age < 0 or age >120:
            raise AgeError(f" age {age} is INNCORECTLY WRONG, choose from 0 to 120.")
        self.age = age
try:
    person = Human("}name{")
    person.get_age(130)
exept AgeError as dg:
print(f"error with {dg}")

#Бетховен не умел не умножать не делить