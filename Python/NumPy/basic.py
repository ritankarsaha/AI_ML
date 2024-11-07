import numpy as np
import time
import sys

'''
a=np.array([1,2,3])
print(a)

'''


# benefits of numpy array is that it takes a lot less memory than a list
l = range(1000)
print(sys.getsizeof(5)*len(l))
array = np.arange(1000)
print(array.size * array.itemsize)
#ofc the latter has much less size



#showing that numpy is faster than the avg list.
SIZE = 1000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)
#python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)] #finds the sum of the firdt element of both thr lists
print("python list took: ", (time.time()-start)*1000)
#numpy array
start = time.time()
result = a1 + a2
print("Numpy list took: ", (time.time()-start)*1000)

# python list took:  0.08606910705566406
# Numpy list took:  0.05507469177246094
# therefore umpy is faster.



#basic numpy manipulation.
a11 = np.array([1,2,3])
a22 = np.array([4,5,6])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)

