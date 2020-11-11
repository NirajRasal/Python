rows = int(input("Enter no of rows:"))
tp = int(input("enter 1 to print upperword and 0 to print downward:"))
typee = bool(tp)                            #type casting int to bool

if typee == True:
 for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end="")
    print()    

else: 
  for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()    

