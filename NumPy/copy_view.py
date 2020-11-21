import numpy as np

arr = np.array([1,2,3,4])
cp = arr.copy()                                 #copied arr to cp

arr[1] = 10                                     #modified original array

print("Original array:",arr)                      #copied array remians same
print("Copied array:",cp)                       
print("*************VIEW Method**************")

ar = np.array([1,2,3,4])    
cop = ar.view()                                  #viewed arr to cp

ar[1] = 10                                      #modified original array

print("Origianl array",ar)                      #viewed array along with original array changes
print("Viewed array",cop)                       

