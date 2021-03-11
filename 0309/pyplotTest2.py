import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,12,0.01)
y = np.sin(t)
#plot : 선 그래프
# plt.plot(t, y,lw=3, label='sin')
# plt.plot(t, np.cos(t),'r', label='cos')
# plt.grid()
# plt.legend()
# plt.xlabel('time')       # x축 라벨 적용하기
# plt.ylabel('Amplitude')  # y축 라벨 적용하기
# plt.title('Example of sinewave')
# plt.show()


# t = np.array([0,1,2,3,4,5,6,7,8,9])
# y = np.array([9,8,7,9,8,3,2,4,3,4])

# colormap = t
# plt.figure(figsize=(10,6))
# plt.scatter(t,y,s=50, c=colormap,  marker='>')
# plt.colorbar()
# plt.show()


s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

# plt.plot(s1, label='s1')
# plt.plot(s2, label='s2')
# plt.plot(s3, label='s3')
# plt.legend()
# plt.show()

plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()