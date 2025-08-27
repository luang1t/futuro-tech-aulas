# import time
# def saudacao(a):
#     return print(f"Olá {a}")

# nome = input("Digite o seu nome: ")

# saudacao(nome)

# def parabens(aniversariante):
#     print(f"Parabéns para você {aniversariante}!")
#     time.sleep(0.5)
#     print("Muitas felicidades")
#     time.sleep(0.5)
#     print("Muitos anos de vidaaa!")
#     time.sleep(0.5)

# aniversariante = input("Digite o seu nome: ")
# parabens(aniversariante)

# def coxinha(preco):
#     print(f"A coxinha está R$:{preco:.2f}")

# preco_coxinha = float(input("Digite o preço: "))
# coxinha(preco_coxinha)

def verificar_positivo(numero):
    if numero > 0:
        return f"Positivo '{numero}' é positivo"
    else:
        return f"Negativo '{numero}' é negativo"
    
verificar_numero = int(input("Digite um numero para saber se ele é positivo"))    
verificar_positivo(verificar_numero)

