import pandas as pd

df = pd.read_csv('survey.csv', encoding='cp949')

# print(df.head())
# print(df.mean())
# print(df.income.mean())
# print(df.income.sum())
# print(df.income.median())
# print(df.describe())#데이터 개수, 평균, 표준편차, 최솟값, 0~25%. 중앙값, 0~75%, 최댓값 
#print(df.jobSatisfaction.describe())
#print(df.sex.value_counts())
#print(df.groupby(df.sex).mean())

# pip install scipy
from scipy import stats

# male = df.income[df.sex=='m']
# female = df.income[df.sex=='f']

# ttest_result = stats.ttest_ind(male,female)

# print(ttest_result)
# print(ttest_result[1])

# if ttest_result[1] > .05:
# 	print('p-value는 ', ttest_result[1],'로 95% 수준에서 유의하지 않음')
# else: 	
# 	print('p-value는 ', ttest_result[1],'로 95% 수준에서 유의함')

corr = df.corr()
print(corr)

print(df.income.corr(df.stress))
corr.to_csv('corr.csv')

