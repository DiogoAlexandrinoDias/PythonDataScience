import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aula4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preço_unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.to_period("M")

st.title("Dashboard de vendas")

st.metric("Total de vendas", f"R$ {df["Receita"].sum():,.2f}")
st.metric("Média por venda", f"R$ {df['Receita'].mean():,.2f}")

categorias = df["Categoria"].unique()
categoria_selecionada = st.selectbox("Selecione a categoria", categorias)
df_filtrado = df[df["Categoria"] == categoria_selecionada]

# Grafico por produto
st.subheader("Receita por produto")
# criar uma figura
fig1, ax1 = plt.subplots()
df_filtrado.groupby("Produto")["Receita"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# Grafico por mes
st.subheader("Receita mensal")
fig2, ax2 = plt.subplots()
df.groupby("Mês")["Receita"].sum().plot(ax=ax2)
st.pyplot(fig2)dir
