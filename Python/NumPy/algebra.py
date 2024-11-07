import numpy as np

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)
print(a.dot(b))
print(np.matmul(a,b))


#finding the determinant of a matrix. The determiannt of an idnetity matrix is always 1 

c = np.identity(8)
print(np.linalg.det(c))

## determinant, trace , singular vector composition, eigenvalues, matrix norm, inverse

##Statistics in NumPy
stats = np.array([[1,2,3],[5,6,7]])
print(np.min(stats, axis = 0)) #for outputting the final min of the all tyhe elements of teh matrix
print(np.min(stats, axis=1)) #for outputting the min element so feach row of the array
print(np.max(stats, axis = 0)) #for outputting the final max of the all tyhe elements of teh matrix
print(np.max(stats, axis=1)) #for outputting the max element so feach row of the array

print(np.sum(stats)) #outputting the sum of all the elements of the array
print(np.sum(stats, axis =0)) # outputting the sum of each rows
print(np.sum(stats, axis=1)) # outputting the sum of each colummns



