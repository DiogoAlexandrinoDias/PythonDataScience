import streamlit as st
import pandas as pd
import plotly.express as px

ALUNO = "Aluno"
DISCIPLINA = "Disciplina"
DATA = "Data_Prova"
NOTA = "Nota"

st.set_page_config(page_title="Dashboard Escolar", layout="wide")
st.title("Dashboard de Desempenho Escolar")

arquivo = st.file_uploader("Envie o arquivo CSV com notas", type=["csv"])

if arquivo:
    try:
        df = pd.read_csv(arquivo)
        df[DATA] = pd.to_datetime(df[DATA])
        df["Mês"] = df[DATA].dt.to_period("M").astype(str)

        media_geral = df[NOTA].mean()
        disciplina_top = df.groupby(DISCIPLINA)[NOTA].mean().idxmax()
        aluno_pior = df.groupby(ALUNO)[NOTA].mean().idxmin()

        col1,col2,col3 = st.columns(3)
        col1.metric("Media geral", f"{media_geral:.2f}")
        col2.metric("Melhor Disciplina", disciplina_top)
        col3.metric("Aluno com menor média", aluno_pior)

        aluno_selecioando = st.selectbox("Filtrar por Alunos:", df[ALUNO].unique())
        df_filtrado = df[df[ALUNO] == aluno_selecioando]

        st.subheader(f"Nota de {aluno_selecioando} por disiciplina")
        fig_bar = px.bar(df_filtrado, x="Disciplina", y="Nota", color="Disciplina", text_auto=True)
        st.plotly_chart(fig_bar, use_container_width=True)# Exibindo Gráfico


        st.subheader("Evolução de Notas por mês")
        fig_linha = px.line(df, x="Mês", y="Nota", color="Aluno", markers=True, title="Notas ao longo do tempo")
        st.plotly_chart(fig_linha, use_container_width=True)
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    st.info("Envie um aquivo CSV com as Colunas: Aluno, disciplina, Data_Prova, Nota")