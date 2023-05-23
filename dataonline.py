import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
def enviar_dados(new_row):
    # define o escopo de acesso
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    # carrega as credenciais do arquivo JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name('projeto-fuga-386622-f2345a1d355c.json', scope)

    # autoriza o acesso com as credenciais
    client = gspread.authorize(creds)

    # abre a planilha pelo nome
    sheet = client.open('Projetofuga').sheet1

    # adiciona a linha na planilha
    sheet.append_row(new_row)

def salvar_dados():
    # define o escopo de acesso
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    # carrega as credenciais do arquivo JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name('projeto-fuga-386622-f2345a1d355c.json', scope)

    # autoriza o acesso com as credenciais
    client = gspread.authorize(creds)

    # abre a planilha pelo nome
    sheet = client.open('Projetofuga').sheet1

    # pega todos os valores da planilha
    values = sheet.get_all_values()

    arr = np.array(values)

    df = pd.DataFrame(arr)

    df.to_csv('Dados.csv', index=False)
