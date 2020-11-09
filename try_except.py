# a = 10
try:
    print(a)
except NameError:           #name of expecption you can also remove the name and it will run fine.
    print('hello world')
finally:                    #execute regarless try or except is get executed or not
    print('hello')