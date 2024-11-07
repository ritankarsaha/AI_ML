import numpy as np
array = np.arange(15).reshape(5,3)


print(array>5)  # masking into boolean values
print(array[array>5])  # prints a linear array of all the eleemnts that are greateer than 5

array2 = np.array([1,2,3,4,56,6,7,7,88,7])
print(array2[[1,2,3,4]]) #prints the elemtns which are presnt at this particular indcies

print(((array2 > 50) & (array2 < 100)))

