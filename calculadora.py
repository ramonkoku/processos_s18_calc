class Calculadora:
    def __init__(self, numero1, numero2):
        self.__numero1 = numero1  # Atributos privados
        self.__numero2 = numero2
    
    def maiorNumero(self):
        if self.__numero1 == self.__numero2:
            return 'Os dois números são iguais'
        elif self.__numero1 > self.__numero2:
            return f'O maior número é {self.__numero1}'
        else:
            return f'O maior número é {self.__numero2}'
    
    def somar(self):
        return self.__numero1 + self.__numero2
    
    def diferenca(self):
        return abs(self.__numero1 - self.__numero2)
