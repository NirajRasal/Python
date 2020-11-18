import numpy as np

arr = np.array([1, 2, 3, 4, 5])  #array
x = arr.copy()
arr[0] = 42

print(arr)      #original array
print(x)        #copied array