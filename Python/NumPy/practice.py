import numpy as np

array1 = np.array([[1,2,3,4,45,4,2,1],[1,2,3,4,5,6,7,8],[11,22,33,44,55,66,77,88],[1,2,3,4,45,4,2,1],[1,2,3,4,45,4,2,1],[1,2,3,4,45,4,2,1],[1,2,3,4,45,4,2,1],[1,2,3,4,45,4,2,1],[1,2,3,4,45,4,2,1]])
print(array1)


#to print  1 2
#          11 22

print(array1[1:3 , 0:2]) #last index is nit takenin into account. the first set is the set of rows and the second set is the set of columns


print(array1[[0,1,2,3,4],[1,2,3,4,5]]) # the first list is the list of the corresponding rows and the second list is the list of the corresponding columns


print(array1[[0,4,5], 3:]) # print the elements of the arrays of the 0th 4th and 5th rows and other eleemtns starting fromt he third column.
