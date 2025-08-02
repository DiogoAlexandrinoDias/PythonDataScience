import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aula4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preço_unitario"]

# summ -> soma
total_receita = df["Receita"].sum()
print("Total de vendas R$", total_receita)

# mean-> media
media_receita = df["Receita"].mean()
print("Média da receita R$", media_receita)

# Produto mais vendido em quantidade
# idxmax -> pegar o maior valor
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
print("Produto mais vendido: ",produto_mais_vendido)

categoria_top_receita = df.groupby("Categoria")["Receita"].sum().idxmax()
print("Categoria com maior receita: ",categoria_top_receita)

# Gráfocp de barras - receitas por categoria

df.groupby("Categoria")["Receita"].sum().plot(kind="bar", title="Receita por categoria")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()

df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M")
df.groupby("Mes")["Receita"].sum().plot(kind="line", title="Receita Mensal")
plt.ylabel("Receita R$")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()