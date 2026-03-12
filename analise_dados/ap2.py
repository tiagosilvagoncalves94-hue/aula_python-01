import streamlit as st
import pandas as pd
import plotly.express as px

#criação de titulo
st.title("Dashboard empresa")

#carregamento dos dados
df = pd.read_csv("novos_dados.csv")
st.subheader("tabela de dados")
st.dataframe(df)

#criação de filtro
departamento = st.selectbox("selecione o departamento: ", df["departamento"].unique())
df_filtrado = df[df["departamento"] == departamento]
st.subheader("dados filtrados")
st.write(df_filtrado)

#Elaboração do gráfico
barra = px.bar(
    df_filtrado,
    x= "nome_completo",
    y= "salario_mensal_brl",
    color= "nome_completo",
    title= "funciónarios"
)

st.plotly_chart(barra)