# test_fibo.py
import unittest ### Importo librería unittest
from fibo import fibonacci ### importo la función de fibonacci del script fibo

class Test(unittest.TestCase):
    def prueba_5ta_pos(self): ### Función para comprobar si el valor de la 5ta posición de la sucesión es = 3
        resultado = fibonacci(5)
        expected = 3
        self.assertEqual(resultado[-1], expected)

if __name__ == '__main__':
    unittest.main()