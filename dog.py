from animal import Animal
class Dog(Animal):

    def __init__(self, eats, animal_sound):
        super().__init__(eats, animal_sound)

    def eat(self):
        return 'Rax eats'
    
    def sound(self):
        return 'Dog barks'

dog_1 = Dog("Food", "Bark")

print(dog_1.eat())
print(dog_1.sound())