import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.

# link curso: https://www.linkedin.com/learning/python-para-ciencia-de-dados-formacao-basica/contando-e-removendo-valores-em-branco

def cria_data_frame():
    em_branco = np.nan
    np.random.seed(25)
    df = DataFrame(np.random.randn(36).reshape(6, 6))
    df.loc[3:5, 0] = em_branco
    df.loc[1:4, 5] = em_branco
    return df


def data_frame_dados_repetidos():
    dados = {
        'coluna1': [1, 1, 2, 2, 3, 3, 3],
        'coluna2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
        'coluna3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
    }
    print()
    return DataFrame(dados)


def data_frame_dados_repetidos2():
    dados = {
        'coluna1': [1, 1, 2, 2, 3, 3, 3],
        'coluna2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
        'coluna3': ['D', 'A', 'B', 'B', 'C', 'C', 'C']
    }
    print()
    return DataFrame(dados)


def data_frame_variavel(quant_dados, linhas, colunas):
    df = pd.DataFrame(np.arange(quant_dados).reshape(linhas, colunas))
    print()
    return df


if __name__ == '__main__':
    # Exercicios:

    print(cria_data_frame())
    print()

    # Aula: Removendo dados duplicados:

    print(data_frame_dados_repetidos())  # --> criando o dataframe

    df = data_frame_dados_repetidos()
    print(df.duplicated())  # --> printando quais linhas estao duplicadas
    print()
    print(df.drop_duplicates())  # --> printa o dataframe sem as linhas duplicadas, porém não altera o dataframe
    print()
    print(df)
    print()
    df.drop_duplicates(inplace=True)  # --> printa o dataframe sem as linhas duplicadas, alterando o dataframe
    print(df)
    print()
    df2 = data_frame_dados_repetidos2()
    print(df2)
    print(df2.drop_duplicates(['coluna3']))  # --> retira as linhas duplicadas levando em consideração somente a coluna3

    # Aula: Concatenando dados:

    df1 = data_frame_variavel(36, 6, 6)
    df2 = data_frame_variavel(15, 5, 3)
    print(df1)
    print(df2)
    print()
    print(pd.concat([df1, df2]))  # --> concatena os dois dataframeas, inserindo as linhas do segundo objeto embaixo do primeiro, considerando os indices das linhas
    print()
    print(pd.concat([df1, df2], axis=1))  # --> concatena os dois dataframeas, inserindo as linhas do segundo objeto embaixo do primeiro, considerando os indices das colunas

