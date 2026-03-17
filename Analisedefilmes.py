import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_movies = pd.read_csv('top-500-movies.csv', sep=',')
print(df_movies)


df_movies1 = df_movies.dropna(inplace=False)
df_movies1 = df_movies1[(df_movies1 != 0).all(axis=1)]
df_movies1 = df_movies1[(df_movies1.astype(str) != '').all(axis=1)]
df_movies1.drop_duplicates(inplace=True)

colunas_numericas = df_movies1.select_dtypes(include=['int64', 'float64'])

matriz_correlacao = colunas_numericas.corr(method='pearson')

plt.figure(figsize=(max(12, len(matriz_correlacao.columns)), max(8, len(matriz_correlacao.columns))))
plt.matshow(matriz_correlacao, fignum=1)
plt.xticks(range(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=90)
plt.yticks(range(len(matriz_correlacao.columns)), matriz_correlacao.columns)
plt.colorbar()
plt.title('Matriz de Correlação', pad=20)
plt.show()


df_movies2 = df_movies1.copy()
df_movies2_valid = df_movies2[['title','production_cost','worldwide_gross']]

higher_PC = df_movies2_valid.nlargest(20, 'production_cost').copy()
higher_WG = df_movies2_valid.nlargest(20, 'worldwide_gross').copy()

higher_PC.reset_index(drop=True, inplace = True)
higher_PC.drop('worldwide_gross', axis=1, inplace=True)
print(higher_PC)

higher_WG.reset_index(drop=True, inplace = True)
higher_WG.drop('production_cost', axis=1, inplace=True)
print(higher_WG)


df_movies3 = df_movies1.copy()
df_movies3_valid = df_movies3[['title','production_cost','worldwide_gross','genre']]

higher_PC3 = df_movies3_valid.nlargest(20, 'production_cost').copy()
higher_WG3 = df_movies3_valid.nlargest(20, 'worldwide_gross').copy()

higher_PC3=higher_PC3[['title','genre']]
higher_WG3=higher_WG3[['title','genre']]
print(higher_PC3)


a = higher_WG3.copy()
a.reset_index(drop=True, inplace=True)
print(a)

df_movies4 = df_movies1.copy()
df_movies4_valid = df_movies4[['title','worldwide_gross']]

higher_WG4 = df_movies4_valid.nlargest(20, 'worldwide_gross').copy()
media_arrecadacao = higher_WG4['worldwide_gross'].mean()
media_arrecadacao
print()
print(f"a media de arrecadação dos 20 maiores filmes com a media mundial é {media_arrecadacao} ")


plt.figure(figsize=(14, 8))
bars = plt.barh(higher_WG4['title'], higher_WG4['worldwide_gross'], color='blue', height=0.6)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width - 0.15 * width,
        bar.get_y() + bar.get_height() / 2,
        f"${width:,.2f}",
        ha='center',
        va='center',
        fontsize=8,
        color='white'
    )

plt.yticks(rotation=0)
plt.ylabel('Filme')
plt.xlabel('Arrecadação Mundial ($)')
plt.title('Distribuição de Arrecadação dos 20 Filmes com Maior Bilheteria Mundial')
plt.tight_layout()

plt.show()

df_movies5 = df_movies1.copy()
df_movies5_valid = df_movies5[['title', 'worldwide_gross', 'domestic_gross']]


higher_WG5 = df_movies5_valid.nlargest(20, 'worldwide_gross').copy()
higher_DG5 = df_movies5_valid.nlargest(20, 'domestic_gross').copy()

combined_df = pd.concat([higher_WG5, higher_DG5]).drop_duplicates(subset=['title']).nlargest(20, 'worldwide_gross')

combined_df['total_gross'] = combined_df['worldwide_gross'] + combined_df['domestic_gross']

plt.figure(figsize=(14, 8))
bars = plt.barh(combined_df['title'], combined_df['total_gross'], color='blue', height=0.6)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width - 0.15 * width,
        bar.get_y() + bar.get_height() / 2,
        f"${width:,.2f}",
        ha='center',
        va='center',
        fontsize=8,
        color='white'
    )

plt.yticks(rotation=0)
plt.ylabel('Filme')
plt.xlabel('Arrecadação Total ($)')
plt.title('Distribuição de Arrecadação Total (Local + Mundial) dos 20 Filmes com Maior Bilheteria')
plt.tight_layout()

plt.show()

df_movies6 = df_movies1.copy()
df_movies6_valid = df_movies6[['title', 'worldwide_gross', 'domestic_gross']]

higher_WG6 = df_movies6_valid.nlargest(20, 'worldwide_gross').copy()
higher_DG6 = df_movies6_valid.nlargest(20, 'domestic_gross').copy()

combined_df = pd.concat([higher_WG6, higher_DG6]).drop_duplicates(subset=['title']).nlargest(20, 'worldwide_gross')
combined_df['total_gross'] = combined_df['worldwide_gross'] + combined_df['domestic_gross']

plt.figure(figsize=(14, 8))

bar_width = 0.25
indices = range(len(combined_df))

plt.barh([i - bar_width for i in indices], combined_df['worldwide_gross'], color='blue', height=bar_width, label='Arrecadação Mundial')
plt.barh(indices, combined_df['domestic_gross'], color='green', height=bar_width, label='Arrecadação Local')
plt.barh([i + bar_width for i in indices], combined_df['total_gross'], color='red', height=bar_width, label='Arrecadação Total')

for i, value in enumerate(combined_df['worldwide_gross']):
    plt.text(value, i - bar_width, f"${value:,.2f}", va='center', ha='right', fontsize=8, color='white')

for i, value in enumerate(combined_df['domestic_gross']):
    plt.text(value, i, f"${value:,.2f}", va='center', ha='right', fontsize=8, color='white')

for i, value in enumerate(combined_df['total_gross']):
    plt.text(value, i + bar_width, f"${value:,.2f}", va='center', ha='right', fontsize=8, color='white')

plt.yticks(indices, combined_df['title'])
plt.ylabel('Filme')
plt.xlabel('Arrecadação ($)')
plt.title('Distribuição de Arrecadação (Mundial, Local e Total) dos 20 Filmes com Maior Bilheteria')
plt.legend()
plt.tight_layout()

plt.show()

total_gross = higher_WG4['worldwide_gross'].sum()
higher_WG4['percentual_participacao'] = (higher_WG4['worldwide_gross'] / total_gross) * 100

plt.figure(figsize=(12, 8))
plt.pie(
    higher_WG4['percentual_participacao'],
    labels=higher_WG4['title'],
    autopct='%1.1f%%',
    startangle=140
)

plt.title('Percentual de Participação dos 20 Filmes com Maior Arrecadação de Bilheteria Mundial')
plt.tight_layout()
plt.show()

df_movies7 = df_movies.copy()
df_movies7_valid = df_movies7[['title','worldwide_gross','year']]


df_movies7_valid = df_movies7_valid.sort_values(by='year', ascending=False)

current_year = pd.Timestamp.now().year
last_25_years = current_year - 25
df_last_25_years = df_movies7_valid[df_movies7_valid['year'] >= last_25_years]

df_total_gross_by_year = df_last_25_years.groupby('year')['worldwide_gross'].sum().reset_index()

df_total_gross_by_year = df_total_gross_by_year.sort_values(by='year')

plt.figure(figsize=(12, 8))
plt.plot(df_total_gross_by_year['year'], df_total_gross_by_year['worldwide_gross'], marker='o', linestyle='-', color='b')

plt.xlabel('Ano')
plt.ylabel('Arrecadação Mundial Total ($)')
plt.title('Evolução da Arrecadação Mundial de Bilheteria nos Últimos 25 Anos')
plt.xticks(df_total_gross_by_year['year'], rotation=45)
plt.grid(True)

plt.show()

df_movies8 = df_movies.copy()
df_movies8_valid = df_movies8[['title','worldwide_gross','genre']]

df_action_movies = df_movies8_valid[df_movies8_valid['genre'].str.contains('Action', case=False, na=False)]

higher_action_movies = df_action_movies.nlargest(20, 'worldwide_gross').copy()
higher_action_movies

media_arrecadacao_action = higher_action_movies['worldwide_gross'].mean()
print(f"A média de arrecadação para os 20 filmes de ação com as maiores arrecadações é: {media_arrecadacao_action:.2f}")

df_movies9 = df_movies1.copy()
df_movies9_valid = df_movies9[['title', 'production_cost','genre']]

df_Adventure_movies = df_movies9_valid[df_movies9_valid['genre'].str.contains('Adventure', case=False, na=False)]
higher_Adventure_movies = df_Adventure_movies.nlargest(20, 'production_cost').copy()
media_arrecadacao_Adventure = higher_Adventure_movies['production_cost'].mean()
print(f"A média de arrecadação para os 20 filmes de aventura com as maiores arrecadações é: {media_arrecadacao_Adventure:.2f}")

total_participacao = df_movies['worldwide_gross'].sum()

grouped = df_movies.groupby('genre')['worldwide_gross'].sum().reset_index()

grouped['percentage'] = (grouped['worldwide_gross'] / total_participacao) * 100

plt.figure(figsize=(12, 8))
plt.bar(grouped['genre'], grouped['percentage'], color='skyblue')
plt.xlabel('Gênero')
plt.ylabel('Percentual de Participação na Bilheteria Mundial')
plt.title('Participação na Bilheteria Mundial por Gênero')
plt.xticks(rotation=45, ha='right')
plt.show()
