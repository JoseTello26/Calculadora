import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        '''Prueba de suma'''
        self.assertEqual(suma(3,2), 3+2)

    def test_resta(self):
        '''Prueba de resta'''
        self.assertEqual(resta(3,2), 3-2)

    def test_multiplicacion(self):
        '''Prueba de multiplicacion'''
        self.assertEqual(multiplicacion(3,2), 3*2)
    def test_division(self):
        '''Prueba de division'''
        self.assertEqual(division(3,2), 3/2)
        self.assertEqual(division(3,0), -1)
if __name__ == '__main__':
    unittest.main()