import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_maiorNumero_iguais(self):
        calc = Calculadora(5, 5)
        resultado = calc.maiorNumero()
        self.assertEqual(resultado, 'Os dois números são iguais')

    def test_maiorNumero_primeiro_maior(self):
        calc = Calculadora(10, 5)
        resultado = calc.maiorNumero()
        self.assertEqual(resultado, 'O maior número é 10')

    def test_maiorNumero_segundo_maior(self):
        calc = Calculadora(5, 10)
        resultado = calc.maiorNumero()
        self.assertEqual(resultado, 'O maior número é 10')

    def test_somar(self):
        calc = Calculadora(7, 3)
        resultado = calc.somar()
        self.assertEqual(resultado, 10)

    def test_diferenca(self):
        calc = Calculadora(5, 10)
        resultado = calc.diferenca()
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()
