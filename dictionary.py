person = {              #key value pair
    'Name':'Niraj',
    'age': '20'
}


name = person['Name']   #get value of specific key
#print(name)

person['age']=21        #modifyed value of key
#print(person)

for x in person:        #returns only keys
    print(x)

print(len(person))      # length of dictionary