import pandas as pd



#1: Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url)

#2: Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

print('8-' * 40)
print(dados.head(7))

print('8-' * 40)
print(dados.tail(5))

#3: Confira a quantidade de linhas e colunas desse DataFrame.

print('8-' * 40)
print(dados.shape)

#4: Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.
print('8-' * 40)
print(dados.dtypes)

print('8-' * 40)
print('8-' * 40)
print('8-' * 40)
print(dados.describe())

