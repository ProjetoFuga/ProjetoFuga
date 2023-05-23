import streamlit as st
import pandas as pd
import datetime as dt
import dataonline
import graficos
from PIL import Image
col1, col2, col3 = st.columns(3)
with col2:
    image = Image.open('red.jpg')
    st.image(image)
def aba(nome, turma):
    menu = ["Rede", "Carniceria", "Atlética", "Casd", "Dep Cult", "ITA Aerodesign", "CEE", "ITAndroids",
            "CASD", "ITA Jr", "AGITA", "ITA Rocket", "evTOL", "ITABits", "ITABaja",
            "Fórmula ITA", "DOO", "DA", "ITARobio", "ACICA", "ITA Finance"]
    iniciativa = st.selectbox("Selecione a iniciativa", menu)
    tipos = ["Comunidade", "Técnica que coda", "Técnica que não coda"]
    kind = st.selectbox("Selecione os tipo da iniciativa", tipos)
    year = dt.datetime.now().year
    sel1 = []
    for x in list(range(-year, -1959)):
        sel1.append("01/03" + "/" + str(-x))
        sel1.append("01/08" + "/" + str(-x))
    data_ent = st.selectbox("Selecione a data de entrada", sel1)
    sel2 = ["Não"]
    for x in list(range(-year, -1959)):
        sel2.append("01/07" + "/" + str(-x))
        sel2.append("01/12" + "/" + str(-x))
    data_saida = st.selectbox("Selecione a data de saída", sel2)
    confirmar = st.button("Adicionar dados")

    if confirmar:
        #Adicionar Dados
        dataonline.enviar_dados([nome, turma, iniciativa, kind, data_ent, data_saida])
        return



st.title("Projeto Fuga de Mentes :brain: Rede_")
tab1, tab2 = st.tabs(["Adicionar", "Gráficos"])
with tab1:
    nome = st.text_input("Nome:")
    turma = st.text_input("Turma:")
    aba(nome, turma)
    #DataFrame
    dataonline.salvar_dados()
    st.write(pd.read_csv("Dados.csv"))
with tab2:
    st.header("")
    graficos.graficos()
