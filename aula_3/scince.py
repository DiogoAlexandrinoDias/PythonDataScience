import pandas as pd 
import matplotlib.pyplot as plt 

# ler o csv
df = pd.read_csv("aula_3/vendas _loja.csv")

# nomes das colunas 
# criar colunas chamda receita
df ["receita"] =  df ["Quantidade"] *df["preço_unitario"]

#dum ->  somar 
total_receita = df ["receita"].sum()
print("Toltal de vendas R$", total_receita) # Total de receita faturamento