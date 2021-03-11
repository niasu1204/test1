import matplotlib.pyplot as plt

x = [1,4,9,16,25,36,49,64]

# plt.plot(x)
# plt.show()

# plt.plot(x,color='r')
# plt.show()

# '-','--','-.',':','.','o','v','^','<','3','4','s',p','*','h','H','+','x'
#  '>','1',2','_','D','','|' 
# plt.plot(x,'d')
# plt.show()

y=[i for i in range(1,9)]

plt.plot(x, color='r')
plt.plot(y, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title("matplot sample")
plt.show()
