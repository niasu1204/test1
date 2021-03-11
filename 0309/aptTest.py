import pandas as pd

df = pd.read_csv('apt.csv', encoding='cp949')

#print(len(df))

#print(df.head())
#print(df.tail())

#print(df.지역)
# 지역           아파트       면적     가격   층
#print(df.아파트[df.면적 > 200])
#면적이 130이상 , 가격이 1억 5천 미만(15000)인 아파트명 출력
#print(df.아파트[(df.면적 > 130 ) & (df.가격 < 15000)])

#print(df.loc[:, ['아파트', '가격']] [df.가격 > 40000])

df['단가'] = df.가격/df.면적

#print(df.loc[:10, ['아파트', '가격','단가']])

# print(df.sort_values(by='가격').loc[:,('가격','지역')])
# print(df.sort_values(by='가격', ascending=False).loc[:,('가격','지역')])

#25억이 넘는 아파트를 면적을 기준으로 오름차순 정렬 후 가격 면적 지역을 출력
#print(df[df.가격>250000].sort_values(by='면적').loc[:,('가격','면적','지역')])

dfF = df[df.지역.str.find('분당')> -1]
print(dfF.mean())

