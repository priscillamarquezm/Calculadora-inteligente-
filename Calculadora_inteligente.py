# Entrada do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


# Menu de operações

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Laço de repetição

while True:
    # Recebendo os números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Menu de operações
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Escolha da operação
    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        resultado = numero1 + numero2
        print(f"Resultado da soma: ", resultado)

    elif escolha == '2':
        resultado = numero1 - numero2
        print(f"Resultado da subtração: ", resultado)

    elif escolha == '3':
        resultado = numero1 * numero2
        print(f"Resultado da multiplicação: ", resultado)

    elif escolha == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado da divisão: ", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif escolha == '5':
        print("Saindo da calculadora.")
        break






