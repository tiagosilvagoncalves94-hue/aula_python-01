import streamlit as st
import pandas as pd
import plotly.express as px

#criação de titulo
st.title("Dashboard de desempenho de Alunos")

#carregamento dos dados
df = pd.read_csv("dados.csv")
st.subheader("tabela de dados")
st.dataframe(df)

#criação de filtro
Curso = st.selectbox("selecione o Curso: ", df["Curso"].unique())
df_filtrado = df[df["Curso"] == Curso]
st.subheader("dados filtrados")
st.write(df_filtrado)

#Elaboração do gráfico
barra = px.bar(
    df_filtrado,
    x= "Aluno",
    y= "Nota",
    color= "Aluno",
    title= "Notas dos alunos"
)

st.plotly_chart(barra)