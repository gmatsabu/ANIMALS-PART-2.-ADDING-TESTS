class Animal:
    def __init__(self,eats,sounds):
    
        self.eats = eats 
        self.sounds = sounds

     
    def eat(self):
        return self.eats
       

    def sound(self):
        return self.sounds
       
dog = Animal("Food ","Barks")
cat = Animal("Food","Meow ")

print (dog.eat())
print(dog.sound())
