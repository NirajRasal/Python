import random

no = (random.randrange(1,100))       #picked random no from 1 to 99
chance = 10

print('Computer has picked random no from 1 to 99')
print('Now its your job to guess the no')
print('you have',chance,'chances left')
print('\n')

while chance > 0:
 print('chances remaning=',chance)
 
 userinput = int(input('your guess:'))
 if userinput > no:
    print('your guess is larger than random no \n')
    chance=chance-1
 elif userinput < no:
    print('your guess is smaller than random no \n')
    chance=chance-1
 else:
    print('CONGRATULATIONS!!!.You have successfully guessed the no \n')
    break
print('GAME OVER!!! \n')