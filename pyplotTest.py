from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

x = [1,4,9,16,25,36,49,64]

# plt.plot(x)
# plt.show()

# 'b','g','r','c','m','y','k','w'
# plt.plot(x,color='r')
# plt.show()

#'-','--','-.',':','.','o','v','^','<','3','4','s',p','*','h','H','+','x'
# '>','1',2','_','D','d','|' 
# plt.plot(x,'or')
# plt.show()

y=[i for i in range(1,9)]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("matplot 예제")
plt.show()