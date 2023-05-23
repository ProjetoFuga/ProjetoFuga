import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
def num_ini(pessoa, tipo = "Qualquer tipo"):
    dados = pd.read_csv("Dados.csv")
    dados.columns = [0, 1, 2, 3, 4, 5]
    dataSaida = None
    dataEntrada = None
    for x in dados.index:
        if dados[0][x] == pessoa and dados[2][x] == "Rede":
            dataSaida = dados[5][x]
            dataEntrada = dados[4][x]
    numIni = 0
    if dataSaida == None:
        return 0
    for x in dados.index:
        if dados[0][x] == pessoa:
            if dados[5][x] == "Não":
                dados.loc[x,5] = "1/1/3000"
    if tipo == "Qualquer tipo":
        if dataSaida == "Não":
            for x in dados.index:
                if dados[0][x] == pessoa and dt.datetime.strptime(dados[5][x], '%d/%m/%Y') > dt.datetime.strptime(dataEntrada, '%d/%m/%Y'):
                    numIni += 1
            return numIni
        for x in dados.index:
            if dados[0][x] == pessoa:
                if dt.datetime.strptime(dados[4][x], '%d/%m/%Y') < dt.datetime.strptime(dataSaida, '%d/%m/%Y') and dt.datetime.strptime(dados[5][x], '%d/%m/%Y') > dt.datetime.strptime(dataEntrada, '%d/%m/%Y'):
                    numIni += 1
        return numIni
    else:
        if dataSaida == "Não":
            for x in dados.index:
                if dados[0][x] == pessoa and dados[3][x] == tipo and dt.datetime.strptime(dados[5][x], '%d/%m/%Y') > dt.datetime.strptime(dataEntrada, '%d/%m/%Y'):
                    numIni += 1
            return numIni
        for x in dados.index:
            if dados[0][x] == pessoa and dados[3][x] == tipo:
                if dt.datetime.strptime(dados[4][x], '%d/%m/%Y') < dt.datetime.strptime(dataSaida, '%d/%m/%Y') and dt.datetime.strptime(dados[5][x], '%d/%m/%Y') > dt.datetime.strptime(dataEntrada, '%d/%m/%Y'):
                    numIni += 1
        return numIni
def saiu(tipo = "Qualquer tipo"):
    dados = pd.read_csv("Dados.csv")
    dados.columns = [0,1,2,3,4,5]
    lista = []
    index = [0,1,2,3,4,5,6]#Número de iniciativas
    values = [0,0,0,0,0,0,0]#Número de pessoas com aquela quantidade de iniciativas
    for x in range(1, len(dados)):
        if dados[0][x] not in lista and dados[2][x] == 'Rede' and dados[5][x] != "Não":
            lista = lista + [dados[0][x]]
            numeroIniciativas = num_ini(dados[0][x], tipo)
            for a in index:
                if a == numeroIniciativas:
                    values[a] = values[a] + 1
                    break
    result = pd.DataFrame(index=index, columns=["Número de Pessoas"])
    result.index.name = "Quantidade de iniciativas"
    result["Número de Pessoas"] = values
    return result["Número de Pessoas"]
def naoSaiu(tipo = "Qualquer tipo"):
    dados = pd.read_csv("Dados.csv")
    dados.columns = [0, 1, 2, 3, 4, 5]
    lista = []
    index = [0, 1, 2, 3, 4, 5, 6]  # Número de iniciativas
    values = [0, 0, 0, 0, 0, 0, 0]  # Número de pessoas com aquela quantidade de iniciativas
    for x in range(len(dados)):
        if dados[0][x] not in lista and dados[2][x] == 'Rede' and dados[5][x] == "Não":
            lista = lista + [dados[0][x]]
            numeroIniciativas = num_ini(dados[0][x], tipo)
            for a in index:
                if a == numeroIniciativas:
                    values[a] = values[a] + 1
                    break
    result = pd.DataFrame(index=index, columns=["Número de Pessoas"])
    result.index.name = "Quantidade de iniciativas"
    result["Número de Pessoas"] = values
    return result["Número de Pessoas"]
def graficos():
    dados = pd.read_csv("Dados.csv")
    dados.columns = [0, 1, 2, 3, 4, 5]
    tipoo = ["Qualquer tipo","Comunidade", "Técnica que coda", "Técnica que não coda"]
    tipo = st.selectbox("Selecione o tipo", tipoo)
    st.subheader("Saiu da Rede")
    st.text("Número de pessoas/ Quantidade de iniciativas")
    st.bar_chart(saiu(tipo))
    st.subheader("Não saiu da Rede")
    st.text("Número de pessoas/ Quantidade de iniciativas")
    st.bar_chart(naoSaiu(tipo))
    st.write(dados)