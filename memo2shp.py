# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:49:24 2021
@author: cadfj
"""

import re
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plot
from shapely.geometry import point


string = input('Copie e cole o texto do seu memorial descritivo aqui:')
EPSG = int(input('EPSG de saída: '))
caminho_saida = input('insira o caminho de saída mais o nome do arquivo com a extensão (ex: C:\geo\shape_python\saida1.shp): ')
texto = re.sub(r'(?<=\d)[.]','', string)
texto_decodificado = re.sub(r'(?<=\d)[,]','.', texto)


ColunaX = (re.findall(r" \d{6}\ | \d{6}\.\d{2,3}", texto_decodificado))
ColunaY = (re.findall(r" \d{7}\ | \d{7}.\d{2,3}", texto_decodificado))

tupla = {'col1':ColunaX,'col2':ColunaY}
df = pd.DataFrame(tupla)
geometry = gpd.points_from_xy(df.col1, df.col2)
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs= EPSG)

df.to_excel(r'C:\geo\csv\teste5.xlsx')
gdf.to_file(caminho_saida)

#print(texto_decodificado)
print(df)

gdf.plot(figsize=(16,14), facecolor='white', edgecolor='black') #ax=ax
plot.title('Coordenadas Memorial')
plot.show()

