import numpy as np
a = np.array([5,6,7,89,9])
print(a[0])
a1 = np.array([1,2],[3,4],[6,7])

print(a1.ndim)  # to find out the diemnsion of the array
print(a1.itemsize) # to find out the itemsiz eof the array
print(a1.dtype) # to find the data type of the array.

a2  = np.array([1,2],[3,4],[6,7] , dtype = np.float64) #change the array explicitly to flaot.
print(a2.itemsize) 

print(a2.size) #generates the size of the array.
print(a2.shape) #dimensions of the array


a3 = np.zeroes((3,4)) #creates an empty array of the following array initialised with zeroes
a4 = np.ones((3,4)) #creates an empty array of the following array initialised with ones
a5 = np.arange(1,5) #5 not belonged here while creating the range from 1 to 4
a6 = np.arange(1,5,2) #create range from 1 to 4 skiping 2 places
a6 = np.linspace(1,5,10) #generate 10 numbers between 1 to 5 that are linearly spaced
a2.reshape(2,3) #re-dimesizes an array to a new dimension 
print(a2)

a2.ravel() #flattens the array
a2.min() #finds the minimum of the array
a2.max() #finds the maximum of the array
a2.sum() # finds the sum of all the elements in the array
a.sum(axis =0) # finds the sum of all the elements in the array along a particular column
a.sum(axis = 1) #finds the sum of all the elements in the array along a particular row
np.sqrt(a2) #finds the square root of all the elements of the array
np.std(a2) # finds the standard deviation



array1 = np.array([1,2],[3,4]) 
array2 = np.array([5,6],[7,8])
sum = array1+array2 #sum of 2 arrays.
matrixpro = a1.dot(a2) #matrix multiplication.



arrayfull = np.full((2,2),99, dtype='float32')
print(arrayfull)  #creating a 2 by 2 array having elements 99


#creating random arrays.

random = np.random.rand(4,2)
print(random)  # create a random array of 4 by 2

random = np.random.random_sample(a.shape)
print(random) # create a random array of a shape in this

randomint = np.random.randint(7, size=(3,3))
print(randomint) # create an array of 7 random integers of 3*3 matrix

iden = np.identity(5)
# create an identity matrix of size 5

hehe = np.array([1,2,3])
r1 = np.repeat(hehe,3,axis=0)
print(r1) # 1 dimensional repetition

hehe1 = np.array([[1,2,3]])
r1 = np.repeat(hehe,3,axis=0)
print(r1) # 2 dimensional repetition


#printing a modified matrix
#creating a modifieed matrix using np arrays
output = np.ones((5,5))
z = np.zeroes(3,3)
z[1,1]=9
output[1:-1,1:-1] = z
print(output)


#to copy shit
a =np.array([1,2,3])
b = a.copy()
print(b)

#find cosines
cos = np.cos(a)
print(cos)







