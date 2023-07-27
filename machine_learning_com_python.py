# -*- coding: utf-8 -*-
"""Machine_Learning_com_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IIJEA0kdB-fH-2hfc9SKRifgG9i_bb--

# 1.1 - Algebra Linear em Python
"""

# algebra linear -> x + 2 = 5 =>> x = 3   (Resolver sistemas de equações lineares.)
# x + y = 10 (infinitas possibilidades de resolução)
# se x = 0 o y = 10
# se x = 2 o y = 8
# Equeação Diofantica

#x + y = 10
#2x+ y = 11 --->>

"""$$ \alpha + \beta = 10$$"""

import numpy as np
import scipy as sc
import sympy as sy
import pandas as pd
import matplotlib.pyplot as plt

# diferenças entre escalar, vetor e matriz
# Escalar é um número (Tensor de ordem 0)-->> x=2
x=2 #Escalar
#Vetor é uma estrutura unidimencional, precisa um plano (cartesiano) (tensor de ondem 1)
#matriz é um plano tridimencional,
x2 = np.array([1,2,3]) # vetor com três elementos escalares
x3 = np.array([[1],[2],[3]]) # Matriz(coluna) com 3 elementos vetores com elementos escalares
x4 = np.array([[1,2,3],[1,2,3],[1,2,3]]) # Matriz quadrada tradicional
print(x2)
print()
print(x3)
print()
print(x4)

lista = [1,2,3,4,5]
#df = pd.DataFrame(lista)  -> irá criar um DataFrame com Index 0
df = pd.DataFrame({'coluna1':lista, 'coluna2':lista})   #-> vai criar com o index coluna 1 {} -> dicionário
df

type(df.coluna1)    #->cada coluna é uma array que é igual a series

lista[:1]

x2+x3   #->combinação linear (somatorio de elementos multiplicados entre si)

# Multiplicar

# arr1 (x,y) arr2 (z,w)  ---> y = z  / arr3 (x, w)
#np.dot ou @
#a.b != b.a
np.dot(x4, x3)

x4@x3

#divisão

#2.x = 4 ---> x=4/2
#>> A.X = Y  ----->> Equação Fundamental da Algebra Linear
x4 / x3

"""#1.1.1 Matrizes Especiais"""

'''
Para os Escalares,
O zero é um elementro neutro para a soma  e subtração
o Um é um elemento neutro na multiplicação e divisão
'''

zeros=np.zeros((3,3))
ones=np.ones((3,3))
print(zeros)
print()
print(ones)

"""#1.1.2 Matrizes Inversas (Matriz Quadrada)"""

x4

"""$$A = \pmatrix{a_{00} & a_{01} & a_{02}\\ a_{10} & a_{11} & a_{12}\\a_{20} & a_{21} & a_{22}}
$$
"""

id = np.eye(3)
id

x4*id

"""$$x  .  x^{-1}  =  1$$

-------
$$Matriz Inversa$$
$$A  .  A^{-1}  =  I -->>> Somente em matrizes quadradas.$$

-----

$$Equação Fundamental da Algebra $$

$$A . X = Y--> Fundamento$$
$$A . A^{-1}.X = A^{-1}. Y--> Multiplica nos dois lados$$
 $$ X = A^{-1} . Y    -->REsultado$$ $$--> Se A for uma matriz quadrada$$
"""

'''
Um número multiplicado pelo se uinverso deve ter o resultado 1
o numero 2, o seu inverso é 1/2
2 * 1/2 = 1
'''

'''
Uma MAtriz multiplicada pelo seu inverso deve gerar uma matriz identidade.
MAtriz A
'''

"""# 1.1.3 Matrizes Pseudo Inversas (não Quadradas)

$$Matrizes Pseudo Inversas$$
$$X = (A.^{T}A)^{-1}A^{T}.Y ---> T = Matriz Transposta$$
"""

x1,y1 = -1,0
x2,y2 = 0,1
x3,y3 = 1,2
x4,y4 = 2,1

x = [x1,x2,x3,x4]
y = [y1,y2,y3,y4]

plt.figure(figsize=(10,5))

plt.scatter(x1,y1, color='green', label='Pares Ordenados (X,Y)')
plt.scatter(x2,y2, color='green')
plt.scatter(x3,y3, color='green')
plt.scatter(x4,y4, color='green')

plt.plot(x,y, label='Gráfico que liga os Pontos')
plt.grid(True)
plt.box(False)
plt.legend()
plt.title('Interpolação da Reta Sobre Todos os Pontos')

#y = mx + n
#0 = -m + n
A = np.array([[-1,1], [0,1], [1,1], [2,1]])
y = np.array([[y1], [y2], [y3], [y4]])

(m,n) = np.dot(np.dot(np.linalg.pinv(np.dot(A.T,A)),A.T),y) # -->X=(A.TA)−1AT.Y

print(m,n)

x1,y1 = -1,0
x2,y2 = 0,1
x3,y3 = 1,2
x4,y4 = 2,1

x = [x1,x2,x3,x4]
y = [y1,y2,y3,y4]

plt.figure(figsize=(10,5))

plt.scatter(x1,y1, color='green', label='Pares Ordenados (X,Y)')
plt.scatter(x2,y2, color='green')
plt.scatter(x3,y3, color='green')
plt.scatter(x4,y4, color='green')

v_x=np.linspace(-1,2)
plt.plot(x,y, label='Gráfico que liga os Pontos')
plt.plot(v_x, m*v_x+n, label='Reta Otimizada pelo Método dos Minimos Quadrados')
plt.grid(True)
plt.box(False)
plt.legend()
plt.title('Interpolação da Reta Sobre Todos os Pontos')

"""# 1.2 Estatística em Python"""



"""# 1.3 Os Primeiros passos em Machine Learning"""

import pandas as pd

df_excel = pd.read_excel("Chess.xlsx", sheet_name = "Chess")

df_csv = pd.read_csv("Tomato.csv", sep = ",")

df_excel.shape

df_csv.shape

df_excel.info()

df_csv.info()

df_csv.tail()

df_excel.tail()

df_excel.describe()

df_csv.describe()

df_excel.describe().T

df_csv.describe().T

df_excel.head()

#visualizar a variaçãos das categorias de dados.
set(df_excel["victory_status"])

df_csv.head()

# a coluna Average mostra a medida minima e máxima do tomate para a função
df_csv.describe()

def categorizar_tomate_media(media):
  if media >= 40 and media <= 70:
    return "tomate medio"
  elif media < 40:
    return "tomate pequeno"
  else:
    return "tomatão"

df_csv["Categoria_Tomate"] = df_csv["Average"].apply(categorizar_tomate_media)

df_csv

df_csv.groupby(["Categoria_Tomate"]).describe()

filtro = df_csv["Average"] < 40
df_csv.loc[filtro]

"""#1.4 Numpy"""

import numpy as np

arr_list = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr_list)

arr_zeros = np.zeros((4, 6))
print(arr_zeros)

arr_ones = np.ones((3, 4))
print(arr_ones)

arr_random = np.random.rand(3, 4)
print(arr_random)

print(arr_random.shape)

arr_random_reshape = arr_random.reshape((4,3))
print(arr_random_reshape)

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr3 = np.array([[9,10], [11,12]])

arr4 = np.concatenate((arr1, arr2, arr3), axis=1)

arr4

arr4_split = np.split(arr4, 2)
arr4_split

arr4_transpose = np.transpose(arr4)
print(arr4_transpose)

arr4_revertido = arr4_transpose.T
print(arr4_revertido)

arr_a = np.array([1,7,27])
arr_b = np.array([1,5,1])

arr_a_b = np.add(arr_a, arr_b)
arr_a_b

arr_sub_a_b = np.subtract(arr_a, arr_b)
arr_sub_a_b

"""#1.5 MatPlotLib"""

import matplotlib.pyplot as plt

df_csv.head()

df_csv.info()

df_csv["Date"] = pd.to_datetime(df_csv["Date"])

df_csv.info()

plt.plot(df_csv["Date"], df_csv["Average"])
plt.xlabel("Data")
plt.ylabel("Média em kilos de Tomates")
plt.title("Média de Tomates ao Longo do Tempo")
plt.show()

df_excel.head()

plt.scatter(df_excel["black_rating"], df_excel["white_rating"])
plt.xlabel("Black")
plt.ylabel("White")
plt.title("Partidas de Peças Brancas e Peças Pretas")
plt.show()

plt.bar(df_csv["Categoria_Tomate"], df_csv["Average"])
plt.xlabel("Categorias de Tomates")
plt.ylabel("Média de Tamanho de Tomates")
plt.title("Médias de Tomates por Categorias")
plt.show()

df_excel.groupby(["victory_status"]).mean().plot(kind="pie", y="turns", autopct="%1.0f%%")
plt.title("Média de Partidas Dentro de Estatus de Vitória")
plt.show()

"""#1.6 Scikit-Learn"""

df_diabetes = pd.read_csv("/content/diabetes.csv", sep = ",")
df_diabetes

from sklearn.model_selection import train_test_split

x = df_diabetes.drop(["Class variable"], axis=1)

x

y = df_diabetes["Class variable"]

y

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)
#30% para teste e o restante para treino

x_train
#70% para treino

x_test
#30% para teste

y_train
#70% para o treino pegando a mesma base para comparação

y_test
#30% para test pegando a mesma base para comparação

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train, y_train)

accuracy = knn.score(x_test, y_test)

accuracy

"""#2 EDA - Exploration Data Analisys"""

df_rs = pd.read_excel("/content/dataset_rolling_stones.xlsx")
df_rs

print("Data Inicial:", df_rs["release_date"].min())

print("Data Final:", df_rs["release_date"].max())

df_rs.isnull().sum()

df_rs.duplicated().sum()

df_rs[df_rs.duplicated()]

df_rs.describe()

df_rs["duração_em_min"] = df_rs["duration_ms"]/60000
df_rs

df_rs.describe()

media_por_album = df_rs.groupby("album")["duração_em_min"].mean()
media_por_album

import matplotlib.pyplot as plt

df_maior_duracao = df_rs.groupby("album")["duração_em_min"].mean().sort_values(ascending=False)
df_maior_duracao

df_maior_duracao.head(25).plot(kind="bar")
plt.xlabel("Albuns")
plt.ylabel("Tempo")
plt.title("Albuns com maior duração média por musica")

top_albuns = df_rs["album"].value_counts().head(10)
plt.barh(top_albuns.index, top_albuns.values)
plt.title("Top 10 albuns com maior número de músicas")
plt.show()

df_rs.info()

df_rs_ultima_decada = df_rs[df_rs["release_date"].between(pd.to_datetime("2011"), pd.to_datetime("2022"))]
df_rs_ultima_decada

df_por_album = df_rs_ultima_decada.groupby("album")["popularity"].sum().sort_values(ascending=False).head(10)
df_por_album

total_popularidade = df_por_album.sum()
df_porcentagem = df_por_album / total_popularidade*100
labels = df_porcentagem.index.tolist()
sizes = df_porcentagem.values.tolist()

figura,grafico = plt.subplots(figsize = (18,6))
grafico.pie(sizes, autopct = "%1.1f%%")
grafico.axis('equal')
plt.title("Porcentagem de Popularidade de albuns na última Década")
plt.legend(labels, loc="best")
plt.show()

"""#2.1 Outliers"""

import seaborn as sns

sns.set(style = "whitegrid")
fig, axes = plt.subplots(figsize=(12,6))
sns.boxplot(x = "duração_em_min", data = df_rs)
axes.set_title("Boxplot")
plt.show()

fig, axes = plt.subplots(figsize=(12,6))
sns.violinplot(x="duração_em_min", data = df_rs, color = "gray")
axes.set_title("Gráfico de Violino")
plt.show()

fig, ax = plt.subplots(figsize = (8,6))
sns.violinplot(x="duração_em_min", data = df_rs, ax=ax, color="lightgray")
sns.boxplot(x = "duração_em_min", data = df_rs, ax=ax, whis = 1.5, color = "Darkblue")
ax.set_title("Visualização Violin e Boxplot")
plt.show()

df_rs.head()

def classifica_musica_aovivo(df_rs):
  if df_rs["liveness"]>= 0.8:
    return True
  else:
    return False

df_rs["ao_vivo"] = df_rs.apply(classifica_musica_aovivo, axis=1)
df_rs.head()

df_rs.groupby("ao_vivo")["ao_vivo"].count()

df_gravado_studio = df_rs[df_rs["ao_vivo"]==False]
df_gravado_aovivo = df_rs[df_rs["ao_vivo"]==True]

print("medias das músicas ao vivo:  ", df_gravado_aovivo["duração_em_min"].mean())

print("medias das múdicas em estudio:  ", df_gravado_studio["duração_em_min"].mean())

fig, ax = plt.subplots(figsize = (8,6))
sns.violinplot(x="duração_em_min", data = df_gravado_studio, ax=ax, color="lightgray")
sns.boxplot(x = "duração_em_min", data = df_gravado_studio, ax=ax, whis = 1.5, color = "Darkblue")
ax.set_title("Visualização Violin e Boxplot")
plt.show()

fig, ax = plt.subplots(figsize = (8,6))
sns.violinplot(x="duração_em_min", data = df_gravado_aovivo, ax=ax, color="lightgray")
sns.boxplot(x = "duração_em_min", data = df_gravado_aovivo, ax=ax, whis = 1.5, color = "Darkblue")
ax.set_title("Visualização Violin e Boxplot")
plt.show()

df_studio = df_gravado_studio.groupby("album")["loudness"].sum()
df_aovivo = df_gravado_aovivo.groupby("album")["loudness"].sum()

fig, axes = plt.subplots(1, 2, figsize=(15,4))

sns.histplot(data = df_studio, bins=20, ax=axes[0])
axes[0].set_title("Soma do barulho dos albuns de Estudio")
axes[0].set_xlabel("barulho")
axes[0].set_ylabel("Frequência")

sns.histplot(data = df_aovivo, bins=20, ax=axes[1])
axes[1].set_title("Soma do barulho dos albuns de aovivo")
axes[1].set_xlabel("barulho")
axes[1].set_ylabel("Frequência")

fig.tight_layout()
plt.show()

plt.figure(figsize=(10,5))

sns.kdeplot(data=df_studio, label="Albuns de Estudio", fill = True)
sns.kdeplot(data=df_aovivo, label="Albuns Ao Vivo", fill = True)

plt.title("Distribuição do Barulho dos Albuns")
plt.xlabel("Barulho")
plt.ylabel("Densidade")
plt.legend()

"""#2.2 Testes estatísticos"""

from scipy.stats import shapiro

stat, p = shapiro(df_studio)
print("Soma do Barulho dos Albuns de Estudio: ")
print("Estatistica de teste: {:.4f}, valor p: {}".format(stat, p))

if p> 0.05:
  print("Não há evidencia sufitciente para regeitar a hipotese de normalidade")
else:
  print("A hipótese de normalidade é rejeitada")

stat, p = shapiro(df_aovivo)
print("Soma do Barulho dos Albuns aovivo: ")
print("Estatistica de teste: {:.4f}, valor p: {}".format(stat, p))

if p> 0.05:
  print("Não há evidencia sufitciente para regeitar a hipotese de normalidade")
else:
  print("A hipótese de normalidade é rejeitada")

from scipy.stats import mannwhitneyu

stat, p = mannwhitneyu(df_studio.sample(len(df_studio)), df_aovivo.sample(len(df_aovivo)), alternative="less")

print("Estatística de teste U: ", stat)
print("Valor p: ", p)

alpha = 0.05
if p<alpha:
  print("Diferença estatísticamente significante")
else:
  print("Não há diferença estatisticamente significante")

media_por_album = df_rs.groupby("album")["valence"].mean().reset_index()

media_por_album = media_por_album.rename(columns = {"valence": "media_valence"})

media_por_album["sentimento"] = ["positivo" if v>0.6 else "negativo" for v in media_por_album["media_valence"]]

media_por_album.groupby("sentimento")["sentimento"].count()

df_resultadofinal = pd.merge(df_rs, media_por_album, on="album")
df_resultadofinal.head()

"""#2.3 Matriz de correlação"""

matriz_correlacao = df_resultadofinal.corr()

correlacao_sentimento = matriz_correlacao["media_valence"]

display(correlacao_sentimento)

sns.heatmap(correlacao_sentimento.to_frame(), annot=True, cmap="coolwarm")
plt.show()

sns.scatterplot(x="media_valence", y="danceability", hue="sentimento", data=df_resultadofinal, palette="coolwarm")
plt.xlabel("Media Valence")
plt.ylabel("Danceability")
plt.title("Relação entre a Valência média e a capacidade de Dança das Músicas")
plt.show()

sns.scatterplot(x="media_valence", y="liveness", hue="sentimento", data=df_resultadofinal, palette="coolwarm")
plt.xlabel("Media Valence")
plt.ylabel("liveness")
plt.title("Relação entre a Valência média e Musicas ao vivo")
plt.show()

"""#3 Feature Engineering"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

dados = pd.read_csv("/content/data.csv", sep = ",")
dados.head()

correlation_matrix = dados.corr().round(2)

fig, ax = plt.subplots(figsize=(8,8))
sns.heatmap(data = correlation_matrix, annot = True, linewidths=.5, ax=ax)

x=dados[["sqft_living", "bathrooms"]].values
y=dados["price"].values

sns.scatterplot(data=dados, x="sqft_living", y="price")

sns.scatterplot(data=dados, x="bathrooms", y="price")

fig, ax = plt.subplots(figsize=(12,4))

ax.scatter(x[:,0], y);
ax.scatter(x[:,1], y);

sns.histplot(data=dados, x="sqft_living", kde=True)

sns.histplot(data=dados, x="bathrooms", kde=True)

hist_variaveis = pd.DataFrame(dados, columns=["sqft_living", "bathrooms"])
hist_variaveis.sqft_living.hist()
hist_variaveis.bathrooms.hist()

scaler = StandardScaler()

x_std = scaler.fit_transform(x)

x_std = pd.DataFrame(x_std, columns = ["sqft_living", "bathrooms"])
x_std.sqft_living.hist()
x_std.bathrooms.hist()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

x=dados[["sqft_living", "bathrooms"]].values
y=dados["price"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=7)

len(x_train)

len(x_test)

scaler = MinMaxScaler()

scaler.fit(x_train)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

x_train_scaled

model = LinearRegression()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)

MAE = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE: ", MAE)
print("r2: ", r2)

model_normal=LinearRegression()
model_normal.fit(x_train, y_train)

y_pred_normal = model_normal.predict(x_test)

MAE = mean_absolute_error(y_test, y_pred_normal)
r2 = r2_score(y_test, y_pred_normal)

print("MAE: ", MAE)
print("r2: ", r2)

"""#3.1 Modelos de Machine Learning"""

import seaborn as sb

imoveis = pd.read_csv("/content/Valorizacao_Ambiental.csv", sep=";")
imoveis

imoveis.shape

imoveis.isnull().sum()

imoveis.describe().round(2)

#identificar e estudar a variavel target. "Valor"
plt.hist(imoveis["Valor"], bins=5)

plt.ylabel("Frequência")
plt.xlabel("Valor")
plt.title("Histograma de Variável Valor")

#aplicar raiz quadrada para ampliar a visibilidade dos dados
imoveis["raiz_valor"] = np.sqrt(imoveis["Valor"])
imoveis.head()

plt.hist(imoveis["raiz_valor"], bins=5)

plt.ylabel("Frequência")
plt.xlabel("Valor")
plt.title("Histograma de Variável Valor")

plt.figure(figsize=(24,20))

plt.subplot(4,2,1)
fig = imoveis.boxplot(column = "Valor")
fig.set_title("")
fig.set_ylabel("Valor em R$")

plt.subplot(4,2,2)
fig = imoveis.boxplot(column = "Area")
fig.set_title("")
fig.set_ylabel("Areas em m2")

plt.subplot(4,2,3)
fig = imoveis.boxplot(column = "IA")
fig.set_title("")
fig.set_ylabel("Idade do Imovel")

plt.subplot(4,2,4)
fig = imoveis.boxplot(column = "Andar")
fig.set_title("")
fig.set_ylabel("Andares no imovel")

plt.subplot(4,2,5)
fig = imoveis.boxplot(column = "DistBM")
fig.set_title("")
fig.set_ylabel("Distância do mar")

plt.subplot(4,2,6)
fig = imoveis.boxplot(column = "Suites")
fig.set_title("")
fig.set_ylabel("Quantidade de Suites")

correlation_matriz = imoveis.corr().round(2)

fig, ax = plt.subplots(figsize=(8,8))
sb.heatmap(data=correlation_matriz, annot=True, linewidths=.5, ax=ax)

