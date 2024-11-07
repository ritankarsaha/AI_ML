import numpy as np
a = np.array([6,7,8]) 
print(a[0:2])  #print all the elements of an array from index 0 to 2
print(a[-1]) # printing the elements from the back of the array.

array1 = np.array([[6,7,8],[7,8,9],[8,9,7]])
print(array1) #print the entire array
print(array1[1,2]) # prints the element at that particular position in the array
print(array1[0:2],2) # print the rows through them.
print(array1[: 1:3]) # iterates through all the rows but takes up onlu 1st and 2nd columns

for cell in array1.flat:
      print(cell) # prints the array in a flat condition

# Define array1
array11 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define array2
array22 = np.array([[6, 7, 8], [7, 8, 9], [8, 9, 7]])
# print the array in a vertical stack
print(np.vstack((array11,array22)))
# print the array in a horizontal stack
print(np.hstack((array11,array22)))
# declaring a new array
arraynew = np.arange(30).reshape(2,15)


print(arraynew)
# horizontal spliting the array
result = np.hsplit(arraynew,3)
print(result[0])
print(result[1])
print(result[2])
#vertical spliting the array
result1 = np.vsplit(arraynew,2)
print(result1[0])
print(result[1])


arrayfinal = np.arange(12).reshape(2,6)
# checks boolean values
b = arrayfinal > 4
# printing boolean values
print(b)
#printing only those elements which satisfy the condition
print(arrayfinal[b])
#replacing the said condition with -1 in its place
print(arrayfinal[b] == -1)