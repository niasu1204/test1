import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

df = pd.read_csv('survey.csv', encoding='cp949')

male = df.income[df.sex == "m"] # 남성
female = df.income[df.sex == "f"] # 여성

#Levene의 등분산 검정 
l_result = stats.levene(male, female)

# 유의 수준 표시하기 
if l_result[1] > .05:
    print('P value는 %f 로 95 수준에서 유의하지 않음' % l_result[1])
else :
    print('P value는 %f 로 95 percent 수준에서 유의함' % l_result[1])


print( '남성', round(male.mean(),2), '여성',round(female.mean(),2),'\n등분산검정 결과 LeveneResult(F) : %.3f \np-value : %.3f' % (l_result))

# model = smf.ols(formula='jobSatisfaction ~ English', data=df)
# result = model.fit()

model = smf.ols(formula='jobSatisfaction ~ English + stress + income', data=df)
result = model.fit()
print(result.summary())
