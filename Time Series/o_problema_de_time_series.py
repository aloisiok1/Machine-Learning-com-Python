# -*- coding: utf-8 -*-
"""O problema de Time Series

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B1i8yMtVPgU4ngn5YR8vsbH6OSwEC3GD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

"""#*Tendência - Direção
#*Sazonalidade - Recorrência das oscilações
#*Resíduo - O que sobra do sinal
"""

df_path="https://raw.githubusercontent.com/carlosfab/datasets/master/electricity_consumption/Electric_Production.csv"
df=pd.read_csv(df_path)
df.head()

df.info()

df.index = pd.to_datetime(df.DATE, format="%m-%d-%Y")

df.info()

df.drop("DATE", inplace=True, axis=1)

df.head()

df.loc["1985-05-01"]

plt.plot(df.index, df.Value)

resultados = seasonal_decompose(df)

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, figsize=(15,10))
resultados.observed.plot(ax=ax1)
resultados.trend.plot(ax=ax2)
resultados.seasonal.plot(ax=ax3)
resultados.resid.plot(ax=ax4)
plt.tight_layout()

"""#Intentificando Estacionária ou não Estacionária

## Teste ADF - (Augmented Dickey Fuller)

  H0 - Hipótese Nula (não Estacionária)
  
  H1 - Hipótese Alternativa (rejeição da hipótese nula)


p/value = 0.05 (5%) , então rejeitamos H0 com um nível de confiança de 95%
"""

from statsmodels.tsa.stattools import adfuller

sns.set_style("darkgrid")

x=df.Value.values

result = adfuller(x)

print("teste ABF")
print(f"Teste Estatistico: {result[0]}")
print(f"p-value: {result[1]}")
print(f"Valores Críticos: ")

for key, value in result[4].items():
  print(f"\t{key}: {value}")

ma = df.rolling(12).mean()

f, ax = plt.subplots()
df.plot(ax=ax, legend=False)
ma.plot(ax=ax, legend=False, color="r")
plt.tight_layout()

df_log = np.log(df)
ma_log=df_log.rolling(12).mean()

ma = df.rolling(12).mean()

f, ax = plt.subplots()
df_log.plot(ax=ax, legend=False)
ma_log.plot(ax=ax, legend=False, color="r")
plt.tight_layout()

df_s=(df_log-ma_log).dropna()

ma_s = df_s.rolling(12).mean()
std=df_s.rolling(12).std()

ma = df.rolling(12).mean()

f, ax = plt.subplots()
df_s.plot(ax=ax, legend=False)
ma_s.plot(ax=ax, legend=False, color="r")
std.plot(ax=ax, legend=False, color="g")
plt.tight_layout()

x_s=df_s.Value.values
result_s = adfuller(x_s)

print("teste ABF")
print(f"Teste Estatistico: {result_s[0]}")
print(f"p-value: {result_s[1]}")
print(f"Valores Críticos: ")

for key, value in result_s[4].items():
  print(f"\t{key}: {value}")

df_diff = df_s.diff(1)
ma_diff = df_diff.rolling(12).mean()

std_diff = df_diff.rolling(12).std()

f, ax = plt.subplots()
df_diff.plot(ax=ax, legend=False)
ma_diff.plot(ax=ax, legend=False, color="r")
std_diff.plot(ax=ax, legend=False, color="g")
plt.tight_layout()

x_diff=df_diff.Value.dropna().values
result_diff = adfuller(x_diff)

print("teste ABF")
print(f"Teste Estatistico: {result_diff[0]}")
print(f"p-value: {result_diff[1]}")
print(f"Valores Críticos: ")

for key, value in result_diff[4].items():
  print(f"\t{key}: {value}")

