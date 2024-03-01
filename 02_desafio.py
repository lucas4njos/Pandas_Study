import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

df = dados.query('@imoveis_comerciais not in Tipo')
df = df.query('Tipo == "Apartamento"')

#1) Calcular a média de quartos por apartamento;
ex01 = df['Quartos'].mean(numeric_only=True)

#2) Conferir quantos bairros únicos existem na nossa base de dados;
ex02 = df.Bairro.nunique()

#3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;
ex03 = df.groupby('Bairro')[['Valor']].mean(numeric_only=True).sort_values('Valor', ascending=False)
ex03 = ex03.head()

#4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel
#mais elevadas
ex03.plot(kind='bar', figsize=(14,10), color = 'blue', edgecolor = 'black')
plt.show()

print(f'Ex01: {ex01}\n\n Ex02: {ex02}\n\n Ex03: {ex03}\n\n')



