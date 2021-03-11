import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import platform
from matplotlib import font_manager, rc

CCTV_Seoul = pd.read_csv('CCTV_in_Seoul.csv',  encoding='utf-8')
# print(CCTV_Seoul.head())
pop_Seoul = pd.read_excel('population_in_Seoul.xls', 
                          header = 2,
                          usecols = 'B, D, G, J, N',)
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', 
                          pop_Seoul.columns[1] : '인구수', 
                          pop_Seoul.columns[2] : '한국인', 
                          pop_Seoul.columns[3] : '외국인', 
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
# print(pop_Seoul.head())

#print(CCTV_Seoul.sort_values(by='소계', ascending=False).head())

CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                        CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전']  * 100

#print(CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head())

pop_Seoul.drop([0], inplace=True)
#print(pop_Seoul.head())

# print(pop_Seoul['구별'].unique())
#print(pop_Seoul[pop_Seoul['구별'].isnull()])
pop_Seoul.drop([26], inplace=True)

pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
# print(pop_Seoul.head())

# 구별       인구수       한국인      외국인      고령자     외국인비율      고령자비율
# 구별    소계  2013년도 이전  2014년  2015년  2016년       최근증가율
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
#print(CCTV_Seoul.head())

data_result = pd.merge(CCTV_Seoul,pop_Seoul, on='구별')

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']


data_result.set_index('구별', inplace=True)
#print(data_result.head())

#cctv와 인구의 상관계수 구하기 : 0.1이하면 무시, 0.3~ 약한 상관관계 0.7~ 뚜렷한 상관관계
#print(np.corrcoef(data_result['고령자비율'],data_result['소계'])) # -0.28078554
#print(np.corrcoef(data_result['외국인비율'],data_result['소계'])) # -0.13607433
#print(np.corrcoef(data_result['인구수'],data_result['소계'])) #0.30634228

#print(data_result.sort_values(by='소계', ascending=False).head(5))
#print(data_result.sort_values(by='인구수', ascending=False).head(5))

#그래프 한글처리

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'g']
plt.figure()
data_result['소계'].sort_values().plot(kind='barh',color = colors, grid=True, figsize=(10,10))
plt.show()

data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
# data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
# plt.show()

# fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
# fx = np.linspace(100000, 700000, 100)
# f1 = np.poly1d(fp1)

# plt.scatter(data_result['인구수'], data_result['소계'], s=50)
# plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
# plt.xlabel('인구수')
# plt.ylabel('CCTV')
# plt.grid()
# plt.show()