class Name:         # class defined using class keyword 
    fullname = 'Niraj Rasal'    #string declared inside class

n = Name()  #class object
print(n.fullname)
#print(fullname)    will not work
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Person:
    def __init__(self, name, age):      #called automatically when object is created
        self.name = name
        self.age = age

p1 = Person('Niraj','20')        #parameter passed to class through object
p2 = Person('Vijay','20')

print(p1.name)          #can create multiple object of same class
print(p1.age)

print('\n')

print(p2.name)
print(p2.age)