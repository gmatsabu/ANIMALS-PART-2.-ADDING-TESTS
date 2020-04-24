import unittest
from animal import Animal
from cat import Cat

class AnimalTests(unittest.TestCase):

    def setUp(self):
        self.cat_1 = Animal('Food', 'Meow')
        self.dog_1 = Animal('Food', 'Bark')
 
    def test_dog_sound(self):
        print('test_dog_sound Passed')
        self.assertEqual('Bark',self.dog_1.sounds)
        
    def test_dog_eats(self):
        print('test_dog_eats Passed')
        self.assertEqual(self.dog_1.eats, 'Food')

    def test_cat_sound(self):
        print('test_cat_sound Passed')
        self.assertEqual(self.cat_1.sounds, 'Meow')

    def test_cat_eats(self):
        print('test_cat_eats Passed')
        self.assertEqual(self.cat_1.eats, 'Food')

if __name__ == "__main__":
    unittest.main()


