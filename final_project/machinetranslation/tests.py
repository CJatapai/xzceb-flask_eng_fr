import unittest
from translator import English_to_French
from translator import French_to_English

class Test01(unittest.TestCase): 
    def test01(self):
        self.assertEqual(English_to_French('Hello'), 'Bonjour')
        

class Test02(unittest.TestCase): 
    def test02(self):
        self.assertEqual(English_to_French(' '), ' ')

class Test03(unittest.TestCase): 
    def test03(self):
        self.assertEqual(French_to_English('Bonjour'), 'Hello')

class Test04(unittest.TestCase): 
    def test04(self):
        self.assertEqual(French_to_English(' '), ' ')

unittest.main()
