# -*- coding: utf-8 -*-
"""classificação de bebida

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XC10WdjTuhWOCGEWkM3Hru0_wumF54JH

##Case Classificando bebidas
Será que é possível classificarmos o tipo de bebida dado alguns atributos como volume, quantidade de calorias e quantidade de cafeína?

Na aula de hoje vamos explorar o dataset caffeine para construirmos um classificador com base em modelos de árvores.

#Atributos
bebida: nome da bebida.

Volume (ml): Quantidade em volume.

Calorias: Quantidade de calorias.

Cafeína(mg): Quantidade de cafeína.

tipo: tipo de bebida. (Café, Bebidas Energéticas, Shots Energéticos, Refrigerantes, Chá, Água)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz

dados = pd.read_csv("/content/caffeine.csv", sep=",")
dados.head(3)

dados.shape

set(dados["type"])

dados.isnull().sum()

sb.histplot(data=dados, x="Volume (ml)")

sb.histplot(data=dados, x="Calories")

sb.histplot(data=dados, x="Caffeine (mg)")

sb.pairplot(dados, vars=["Volume (ml)", "Calories", "Caffeine (mg)"], hue="type")

x=dados.drop(columns=["type", "drink"])
y=dados["type"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, stratify=y, random_state=7)

y_test.shape

dt=DecisionTreeClassifier(random_state=7, criterion="gini", max_depth=3)

dt.fit(x_train, y_train)

y_predito = dt.predict(x_test)

tree.plot_tree(dt)

class_names = ['Coffee', 'Energy Drinks', 'Energy Shots', 'Soft Drinks', 'Tea', 'Water']
label_names = ['Volume (ml)',	'Calories',	'Caffeine (mg)'	]

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (15,15), dpi=300)

tree.plot_tree(dt,
               feature_names = label_names,
               class_names=class_names,
               filled = True)

fig.savefig('imagename.png')

print(accuracy_score(y_test, y_predito))

dados['type'].value_counts()

"""Se as variáveis target do seu modelo de decision tree não estão equilibradas, isso pode afetar a precisão e a acurácia do seu modelo, especialmente se a classe minoritária é importante para o seu problema.

Utilize algoritmos que são robustos a desequilíbrios de classe: Alguns algoritmos de machine learning são projetados para serem robustos a desequilíbrios de classe. Alguns exemplos incluem o Random Forests.

Existem algumas técnicas que podem ser usadas para equilibrar classes com um modelo de Random Forest. Duas abordagens comuns são o ajuste do parâmetro class_weight e a aplicação de técnicas de reamostragem.

O parâmetro class_weight permite atribuir pesos diferentes às classes no modelo de Random Forest. Ele pode ser ajustado para dar mais peso às classes minoritárias, ajudando a equilibrar o modelo. Você pode definir o valor do parâmetro "class_weight" como "balanced", o que fará com que o modelo ajuste automaticamente os pesos de acordo com a frequência de cada classe.

Técnicas de reamostragem: Outra abordagem comum é usar técnicas de reamostragem, como oversampling e undersampling, para equilibrar as classes. Oversampling envolve a duplicação ou triplicação de observações da classe minoritária, enquanto undersampling envolve a redução do número de observações da classe majoritária. Isso ajuda a garantir que o modelo seja treinado com um número igual de observações para cada classe.

Você pode experimentar essas técnicas individualmente ou combiná-las para obter melhores resultados em termos de equilíbrio de classes em seu modelo de Random Forest. É importante lembrar que o ajuste correto de hiperparâmetros é fundamental para obter bons resultados em qualquer modelo de machine learning.
"""

from imblearn.over_sampling import SMOTE

# Aplicar SMOTE para oversampling da classe minoritária
oversample = SMOTE()
x_train_os, y_train_os = oversample.fit_resample(x_train, y_train)

"""Nesse exemplo, SMOTE é utilizado para gerar dados sintéticos e equilibrar as classes antes de ajustar o modelo de Random Forest. Note que o método fit_resample é utilizado para aplicar o oversampling na classe minoritária. Por fim, o modelo é avaliado com a métrica de acurácia no conjunto de teste.

Oversampling envolve a criação de mais exemplos para a classe minoritária, aumentando sua representação no conjunto de dados. As técnicas comuns de oversampling incluem a replicação de exemplos existentes (cópia de exemplos da classe minoritária), a geração sintética de novos exemplos com base em exemplos existentes, como a técnica SMOTE (Synthetic Minority Over-sampling Technique), ou a combinação de ambas as abordagens.
"""

x_train.shape

x_train_os.shape

rf = RandomForestClassifier(criterion= 'entropy', n_estimators=80, max_depth = 7, class_weight = 'balanced', random_state=7)

rf.fit(x_train_os, y_train_os)

estimator_rf = rf.estimators_

y_predito_random_forest = rf.predict(x_test)

print(accuracy_score(y_test, y_predito_random_forest)) #relatório de validação das métrica de desempenho.

print (rf.score(x_train, y_train))
print(rf.score(x_test, y_test))

