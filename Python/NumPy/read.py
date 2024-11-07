import numpy as np
x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9,]],np.int32)
np.savetxt("test.txt", x)
y = np.loadtxt("test.txt")
print(y)


filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)
