b = float(input("Digite o valor de B "))
a = float(input("Digite o valor de A "))
c = float(input("Digite o valor de C "))

b2 = b**2

d = b2 - 4 * a * c

raizD = d**0.5

bMenos = -b + raizD
bMais = -b - raizD

e = 2 * a

x1 = bMenos / e
x2 = bMais / e

print(f"Delta: {d}")

if d < 0:
    print("Não existe x1 e x2")
else:
    print(f"X1: {x1}")
    print(f"X2: {x2}")
    print(f"Delta: {d}")
