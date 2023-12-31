# -*- coding: utf-8 -*-
"""Modelo de classificação

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ay72LPBqcxLDKqxhXdsPAIv5kv_lunzY

#1.
"""

import pandas as pd

dados = pd.read_excel("/content/gaf_esp.xlsx")
dados.head()

dados.tail()

dados.describe()

dados.shape

dados.groupby("Espécie").describe()

dados.plot.scatter(x="Comprimento do Abdômen", y="Comprimento das Antenas")

from sklearn import *
#ou para imporar especificamente uma parte da bibilioteca -->
from sklearn.model_selection import train_test_split

x = dados[["Comprimento do Abdômen", "Comprimento das Antenas"]]
y = dados["Espécie"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, stratify=y, random_state=42) #stratify é usado para dividir os dados proporcionalmente

list(y_train).count("Gafanhoto")

list(y_train).count("Esperança")

len(x_train)

len(x_test)

y_train

y_test

from sklearn.neighbors import KNeighborsClassifier

modelo_classificador = KNeighborsClassifier(n_neighbors=3)

modelo_classificador.fit(x_train, y_train)

modelo_classificador.predict([[8,6]])

y_predito = modelo_classificador.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_true=y_test, y_pred=y_predito)

