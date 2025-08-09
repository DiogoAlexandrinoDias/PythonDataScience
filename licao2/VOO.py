"""
Análise de Dados de Voos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de estilo
plt.style.use("seaborn-v0_8")
sns.set_palette("Set2")

# Carregar o CSV (caminho corrigido)
df = pd.read_csv("dados_voos.csv")

# -----------------------------
# ESTATÍSTICAS BÁSICAS
# -----------------------------

# 1. Preço médio das passagens
preco_medio = df["Preco_R$"].mean()

# 2. Mediana da duração dos voos
mediana_duracao = df["Duracao_min"].median()

# 3. Companhia com maior preço médio
companhia_mais_cara = df.groupby("Companhia")["Preco_R$"].mean().idxmax()

# 4. Atraso médio dos voos
atraso_medio = df["Atraso_min"].mean()

# 5. Valor máximo e mínimo dos preços
preco_max = df["Preco_R$"].max()
preco_min = df["Preco_R$"].min()

# 6. Mês com maior preço médio
mes_mais_caro = df.groupby("Mes")["Preco_R$"].mean().idxmax()

# 7. Origem com maior atraso médio
origem_maior_atraso = df.groupby("Origem")["Atraso_min"].mean().idxmax()

# 8. Companhia com menor duração média de voo
companhia_mais_rapida = df.groupby("Companhia")["Duracao_min"].mean().idxmin()

# 9. Rota mais frequente
df["Rota"] = df["Origem"] + " -> " + df["Destino"]
rota_mais_frequente = df["Rota"].value_counts().idxmax()

# 10. Diferença de preço médio entre companhia mais cara e mais barata
precos_por_companhia = df.groupby("Companhia")["Preco_R$"].mean()
diferenca_precos = precos_por_companhia.max() - precos_por_companhia.min()

# -----------------------------
# GRÁFICOS
# -----------------------------

# 11. Gráfico de barras: preço médio por companhia
plt.figure(figsize=(10, 5))
precos_por_companhia.sort_values().plot(kind="bar", title="Preço médio por Companhia")
plt.ylabel("Preço R$")
plt.xlabel("Companhia")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 12. Boxplot: distribuição dos preços por mês
plt.figure(figsize=(10, 5))
sns.boxplot(x="Mes", y="Preco_R$", data=df)
plt.title("Distribuição de Preços por Mês")
plt.xlabel("Mês")
plt.ylabel("Preço R$")
plt.show()

# 13. Histograma: distribuição das durações dos voos
plt.figure(figsize=(8, 5))
plt.hist(df["Duracao_min"], bins=20, edgecolor='black')
plt.title("Distribuição das Durações dos Voos")
plt.xlabel("Duração (min)")
plt.ylabel("Frequência")
plt.show()

# 14. Mapa de calor: correlação entre preço, duração e atraso
plt.figure(figsize=(6, 4))
correlacoes = df[["Preco_R$", "Duracao_min", "Atraso_min"]].corr()
sns.heatmap(correlacoes, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação entre Preço, Duração e Atraso")
plt.show()

# 15. Relação entre duração e preço
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Duracao_min", y="Preco_R$", hue="Companhia", data=df)
plt.title("Relação entre Duração e Preço")
plt.xlabel("Duração (min)")
plt.ylabel("Preço R$")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 16. Atraso médio por mês
plt.figure(figsize=(8, 5))
df.groupby("Mes")["Atraso_min"].mean().plot(marker='o', title="Atraso médio por Mês")
plt.xlabel("Mês")
plt.ylabel("Atraso médio (min)")
plt.show()

# 17. Atraso médio por companhia
plt.figure(figsize=(10, 5))
df.groupby("Companhia")["Atraso_min"].mean().sort_values().plot(kind="bar", title="Atraso médio por Companhia")
plt.ylabel("Atraso médio (min)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 18. Boxplot para identificar outliers de preços por companhia
plt.figure(figsize=(10, 5))
sns.boxplot(x="Companhia", y="Preco_R$", data=df)
plt.title("Análise de Outliers de Preço por Companhia")
plt.xticks(rotation=45)
plt.show()

# -----------------------------

# https://www.google.com/url?sa=i&url=http%3A%2F%2Faconfr4ria.blogspot.com%2F2016%2F12%2Fryukendo-as-sensacionais-cronicas.html&psig=AOvVaw1UlwG-fvDUa6fgsVZpobs2&ust=1754850859975000&source=images&cd=vfe&opi=89978449&ved=0CBgQjhxqFwoTCNjosrav_o4DFQAAAAAdAAAAABAE
https://www.google.com/url?sa=i&url=http%3A%2F%2Faconfr4ria.blogspot.com%2F2016%2F12%2Fryukendo-as-sensacionais-cronicas.html&psig=AOvVaw1UlwG-fvDUa6fgsVZpobs2&ust=1754850859975000&source=images&cd=vfe&opi=89978449&ved=0CBgQjhxqFwoTCNjosrav_o4DFQAAAAAdAAAAABAE
# IMPRESSÃO DOS RESULTADOS
# -----------------------------

print("\n--- RESPOSTAS ---")
print(f"1. Preço médio das passagens: R$ {preco_medio:.2f}")
print(f"2. Mediana da duração dos voos: {mediana_duracao} min")
print(f"3. Companhia com maior preço médio: {companhia_mais_cara}")
print(f"4. Atraso médio dos voos: {atraso_medio:.2f} min")
print(f"5. Valor máximo e mínimo dos preços: R$ {preco_max:.2f}, R$ {preco_min:.2f}")
print(f"6. Mês com maior preço médio: {mes_mais_caro}")
print(f"7. Origem com maior atraso médio: {origem_maior_atraso}")
print(f"8. Companhia com menor duração média: {companhia_mais_rapida}")
print(f"9. Rota mais frequente: {rota_mais_frequente}")
print(f"10. Diferença de preço médio entre companhia mais cara e mais barata: R$ {diferenca_precos:.2f}")
