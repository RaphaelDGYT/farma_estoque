import pandas as pd
from datetime import datetime

def converter_df(df):
    df_convertido = []
    for i in df.index:
        dados = ()
        for j in df.loc[i]:
            dados += (j,)
        df_convertido.append(dados)
    return df_convertido

def tratamento_data(data=list()):
    data_formatada = []
    for i in data:
        i = i.strftime("%d/%m/%Y")
        i = i[3:]
        data_formatada.append(i)
    return data_formatada