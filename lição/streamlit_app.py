import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Dashboard de Notas", layout="centered")

st.title("📊 Dashboard de Notas")

# Verifica se o CSV existe
if not os.path.isfile("dados.csv"):
    st.warning("Nenhum dado encontrado. Use o app de entrada para adicionar registros.")
    st.stop()

# Carrega os dados
df = pd.read_csv("dados.csv")

# Métricas básicas
st.metric("Total de Registros", len(df))
st.metric("Nota Média", f"{df['Nota'].mean():.2f}")

# Tabela dos últimos registros
st.subheader("📋 Últimos registros")
st.dataframe(df.tail(10))

# Gráfico: distribuição das notas
st.subheader("📈 Distribuição das notas")
fig, ax = plt.subplots()
df["Nota"].plot(kind="hist", bins=10, ax=ax)
ax.set_xlabel("Nota")
st.pyplot(fig)

# Gráfico de barras por nome (média de nota por aluno)
if st.checkbox("Mostrar gráfico por nome"):
    st.subheader("📊 Nota média por aluno")
    fig2, ax2 = plt.subplots()
    df.groupby("Nome")["Nota"].mean().sort_values().plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Nota Média")
    st.pyplot(fig2)
