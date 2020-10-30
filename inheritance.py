class Person:                               #parent class
    def __init__(self, name, age):      
        self.name = name
        self.age = age

    def printname(self):                    #parent class method
        print(self.name, self.age)

p = Person('Ajay','34')                     #parent class object
p.printname()   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Student(Person):                      #child class
    pass

s = Student('Vijay','20')                   #child class object
s.printname()                               #parent class method