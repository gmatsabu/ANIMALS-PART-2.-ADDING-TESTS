from animal import Animal

class Cat(Animal):
    def __init__(self, eats, sounds):
        super().__init__(eats, sounds)

    def eat(self):
        return 'Stormy eats'
    
    def sound(self):
        return 'cat meows'

cat_1 = Cat("Food", "Meow")

print(cat_1.eat())
print(cat_1.sound())