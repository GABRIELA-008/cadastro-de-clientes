import streamlit as st
st.title("Cadastro de clientes")

nome = st.text_input("digite o nome do cliente:")
endereco = st.text_input("digite o endereço do cliente:")
data_de_cadastro = st.date_input("Escolha a data de cadastro:")
tipo_cliente = st.selectbox("tipo do cliete",["Pessoa física","Pessoa juridica"])
botao_cadastro = st.button("cadastrar cliente")

if botao_cadastro:
    with open("clientes.csv","a") as arquivo:
        arquivo.write(f"{nome},{endereco},{data_de_cadastro},{tipo_cliente}")
        st.success("cliente cadastrado com sucesso ")