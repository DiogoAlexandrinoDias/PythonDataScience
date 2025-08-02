print("###############################")
print("Calculadora do SENAI")
print("Digite a operação a realizar")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Resto")
print("###############################")

opcao = int(input(""))

if opcao == 1:
    num1 = float(input("Digite o primiero numero:"))
    num2 = float(input("Digite o segundo numero:"))

    result = num1 + num2
    print(f"O seu resultado é: {result}")

elif opcao == 3:
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero"))

    result = num1 * num2
    print(f"O seu resultado é: {result}")

elif opcao == 3:
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero"))

    result = num1 - num2
    print(f"O seu resultado é: {result}")
elif opcao == 4:
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero"))

    result = num1 / num2
    print(f"O seu resultado é: {result}")
elif opcao == 5:
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero"))

    result = num1 % num2
    print(f"O seu resultado é: {result}")
