import numpy as np

# a = np.array([[2,3],[5,2]])
# print(a)
# print(type(a))
  
# d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
# print(d)

# print(d[1][2])
# print(d[1,2])
# print(d[1:,3:])

# d = np.array([2,3,4,5,6])
# print(d)
# print(d.shape)
# e = np.array([[1,2,3,4],[3,4,5,6]])
# print(e.shape)

# print(d.dtype)

# data = np.arange(1,5)
# print(data)
# print(data.dtype)

# b = data.astype('float64')
# print(b)
# print(data)

# z = np.zeros((2,10))
# print(z)
# print(z.dtype)

# o = np.ones((2,10))
# print(o)
# print(o.dtype)

# a = np.ones((2,3))
# b = np.transpose(a)
# print(b)

arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[12,23,14],[36,47,58]])

# print(arr1+arr2)
# print(arr1*arr2)
# print(arr1/arr2)

arr3 = np.array([100,200,300])
# print(arr3.shape)
# print(arr1.shape)
# print(arr1+arr3)

# arr4 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1+arr4)# 에러. 행이나 열중 하나의 크기는 일치해야 한다.

# arr5 = np.array([[9],[3]])
# print(arr1+arr5)


d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
d_list = [[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]]     

#d_list[:2] = 0
d[:2] = 0
#print(d)

arr6 = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
print(arr6)

print(arr6[:4])
print(arr6[-3:])

print(arr1[1,2])
print(arr1[:,2])




