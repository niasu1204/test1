import pandas as pd
#서울시 구별 CCTV 현황
#CCTV_Seoul = pd.read_csv('CCTV_in_Seoul.csv',  encoding='utf-8')
#print(CCTV_Seoul.head())

#print(CCTV_Seoul.columns)

#CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'}, inplace=True)
#print(CCTV_Seoul.head())

#엑셀파일 읽기 - 서울시 인구현황   
# pip install xlrd
#pop_Seoul = pd.read_excel('population_in_Seoul.xls')
#print(pop_Seoul.head())

pop_Seoul = pd.read_excel('population_in_Seoul.xls', 
                           header = 2,
                           usecols = 'B, D, G, J, N')
# print(pop_Seoul.head())


pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', 
                          pop_Seoul.columns[1] : '인구수', 
                          pop_Seoul.columns[2] : '한국인', 
                          pop_Seoul.columns[3] : '외국인', 
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
#print(pop_Seoul.head())                          

