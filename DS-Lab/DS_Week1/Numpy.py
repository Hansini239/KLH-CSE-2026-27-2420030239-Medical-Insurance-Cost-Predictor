import numpy as np
# n = np.array([[1,2],[3,4]])
# # print(n[3])
# print(n[1,-1])

# p = np.array([[1,2],[3,4],[5,6]])
# print(p)
# print(n.ndim)
# print(p.ndim)
# print(p[0,1])

# p = np.zeros([3,4])
# p = np.zeros([1])
# print(p)

# p1 = np.ones([3,4])
# p2 = np.ones([1])
# print(p1)
# print(p2)

# n = np.array([1,2,3,4])
# print(n[0:])
# print(p.shape)
# m = p.reshape(2,2)
# m1 = p.reshape(2,3)
# print(n.reshape(2,2))
# print(m)

# for i in p:
#     print(i)

#concatenate

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = np.concatenate((a,b))
# print(c)

# d = np.array_split(c,5)
# print(d)
# print(d[2])
# print(len(d))
# for i in range(len(d)):
#     print(d[i])

n1 = np.array([1,2,3,4,5])
x = np.where(n1==1) #index
print(x)

n2 = np.array([9,10,7,1,2])
p2 = np.sort(n2)
print(p2)

m = np.array(['java','z','python'])
m1 = np.sort(m)
print(m1)

y = (np.sum([n1,n2],axis=0))
z = (np.multiply(n1,n2))
print(z)
print(y)