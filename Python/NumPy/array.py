import numpy as np


a = np.range(12).reshape(3,4)
# prints the array in the flatten order line by line
for cell in a.flatten():
    print(cell)

# does the same thing as the flatten fucntion. prints the entire order line by line in the column fucntion
for x in np.nditer(a,order='C'):
    print(x)


# prints the thing in the Fortran type and not column type
for x in np.nditer(a,order='F'):
    print(x)

# prints the array after computing all the elements of the array to it's square.
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x


# iterates over both the arrays simultaneously
b = np.arange(3,15,4).reshape(3,1)
for x,y in np.nditer([a,b]):
    print(x,y)