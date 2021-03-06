# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:30:23 2019

@author: Sergio
"""

#Importar librerías de yfinance
import yfinance as yf
ticker = "GGAL.BA"
data = yf .download(ticker, period='2y')
#
#
data['Non_trading_gap'] = data.Open - data.Close.shift(-1)
# Construye nueva columna con Ganancia en tiempo no No Operable
data['Trading_sigma'] = data.High - data.Low
# Construye columna con datos de la volatilidad diaria
#Esta es la máxima valuación positiva de rango para el día. Siempre
data['Trading_today_earning'] = data.Close - data.Open
# Construye columna con ganancia/pérdida en tiempo de operatoria
print(data.head(4))
print('\n--Describe--\n', data.describe())
print('\n--Columns--\n', data.columns)

print('\n--Gráfico con volatilidad diaria--')
import matplotlib.pyplot as plt
plt .style.use('dark_background')
plt.rcParams['figure.figsize'] = [12.0, 5]
data['Trading_sigma'].plot(kind='line',title='Volatilidad diaria')
'''
HOMEWORK-Tareas para el hogar
Analizar el cuartil superior menos el cuartil inferior
Esto daría un cuartil central donde el 50% de los valores 
operados en las últimas (period) ruedas que generan la oportunidad de 
ir LONG (75%MAX menos 75%MIN) luego de identificar apropiadamente
el recorrido de la rueda del día no concluído
'''


