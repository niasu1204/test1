import numpy as np

discount = .05  # 할인율 5%
cashflow = 100 # 현금 100억

# n년차 자본의 현재 가치
def presentvalue(n):
    return (cashflow/((1+discount)**n))

print(presentvalue(1))

for i in range(20):
    print(presentvalue(i))

