import numpy as np
# Estatística
from statistics import mode

# Sequência numérica
dados = [10, 12, 10, 14, 15, 15, 20]

# Média -> tendência central
media = np.mean(dados)

# Mediana -> valor central, robusta contra outliers
mediana = np.median(dados)

# Moda -> valor mais frequente
moda = mode(dados)

# Desvio padrão -> medida de dispersão
desvio_padrao = np.std(dados)

# Variância -> quadrado do desvio padrão
variancia = np.var(dados)


print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desvio padrão: {desvio_padrao}")
print(f"variancia: {variancia}")

