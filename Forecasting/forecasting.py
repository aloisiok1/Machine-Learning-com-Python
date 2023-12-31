# -*- coding: utf-8 -*-
"""Forecasting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12mbfnq1tiWy9qDX_oFkXCskeDyebE7Y1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

"""train.csv
The training data, comprising time series of features store_nbr, family, and onpromotion as well as the target sales.
# - store_nbr identifies the store at which the products are sold.
# - family identifies the type of product sold.
# - sales gives the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips).
# - onpromotion gives the total number of items in a product family that were being promoted at a store at a given date.
"""

df_novo=pd.read_csv("/content/train.csv", index_col="id", parse_dates=["date"])
df_novo

df_novo.info()

df_novo["store_nbr"].nunique()

df_1 = df_novo.loc[df_novo["store_nbr"]==1, ["date", "family", "sales"]]
df_1 = df_1.rename(columns={"date": "ds", "sales":"y", "family":"unique_id"})

df_1

!pip install statsforecast

treino = df_1.loc[df_1["ds"]<"2014-01-01"]
valid = df_1.loc[(df_1["ds"]>="2014-01-01")&(df_1["ds"]<"2014-04-01")]
h = valid["ds"].nunique() #validação do período "valid" (3meses)

h

#erro percentual médio (MAPE) e (WMAPE) -> erro através de pesos
def wmape(y_true, y_pred):
  return np.abs(y_true-Y-pred).sum()/np.abs(y_true).sum()

from statsforecast import StatsForecast
from statsforecast.models import Naive

