import tkinter
from tkinter import ttk
from calculadora import Calculadora

def calcular():
    # Convertendo as entradas para inteiros
    num1 = int(numero1.get())
    num2 = int(numero2.get())

    # Criando a instância da classe Calculadora
    calc = Calculadora(num1, num2)

    # Chamando os métodos da instância
    texto_maior_numero = calc.maiorNumero()
    resultado_maior_label.config(text=texto_maior_numero)

    soma = calc.somar()
    resultado_soma_label.config(text=f'A soma dos dois números é: {soma}')

    diferenca = calc.diferenca()
    resultado_diferenca_label.config(text=f'A diferença entre os dois números é: {diferenca}')

# Criando a janela principal
janela = tkinter.Tk()
janela.title("Calculadora Simples")
janela.geometry('800x400')

# Criando as caixas de entrada
numero1 = ttk.Entry(janela)
numero1.pack()
numero2 = ttk.Entry(janela)
numero2.pack()

# Criando o botão
botao_calcular = ttk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack()

# Criando um label para mostrar o maior número
resultado_maior_label = ttk.Label(janela, text="")
resultado_maior_label.pack()

# Criando um label para mostrar o resultado da soma
resultado_soma_label = ttk.Label(janela, text="")
resultado_soma_label.pack()

# Criando um label para mostrar a diferença entre os dois números
resultado_diferenca_label = ttk.Label(janela, text="")
resultado_diferenca_label.pack()

# Iniciando a aplicação
janela.mainloop()
