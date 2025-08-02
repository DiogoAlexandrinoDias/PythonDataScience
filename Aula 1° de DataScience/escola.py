n1 = int(input("Digita sua nota: "))
n2 = int(input("Digita sua nota: "))
n3 = int(input("Digita sua nota: "))
n4 = int(input("Digita sua nota: "))

soma = n1 + n2 + n3 + n4
media = soma / 4

if media < 7:
    print(f"Reprovado, sua media é {media}")
    
else:
    print(f"Aprovado, sua media é {media}")