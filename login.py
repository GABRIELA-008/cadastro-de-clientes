import streamlit as st
import csv 
import pandas as pd
st.title("Cadastro de clientes")

nome = st.text_input("digite o nome do cliente:")
endereco = st.text_input("digite o endereço do cliente:")
data_de_cadastro = st.date_input("Escolha a data de cadastro:")
tipo_cliente = st.selectbox("tipo do cliete",["Pessoa fisica","Pessoa juridica"])
botao_cadastro = st.button("cadastrar cliente")

if botao_cadastro:
    with open("clientes.csv","a") as arquivo:
        arquivo.write (f"{nome},{endereco},{data_de_cadastro},{tipo_cliente}. \n") 
        st.success("cliente cadastrado com sucesso ") 

st.subheader("Clientes Cadastrados")

try:
    df = pd.read_csv("clientes.csv", encoding_errors="replace", header=None, names=["Nome", "Endereço", "Data de Cadastro", "Tipo de Cliente"])
   
    if df.empty:
        st.warning("O ficheiro está vazio. Nenhum cliente encontrado.")
    else:
        st.dataframe(df)

except FileNotFoundError:
    st.warning("Ainda não há clientes cadastrados.")