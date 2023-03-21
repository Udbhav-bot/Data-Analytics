import random

print ('Random number generation')
print('Enter y to generate a new random number')
while input ('genrate [y/n]:')=='y':
    number = random.randint(1000,9999)
    print(f'lucky number : {number}')
print('Thanks for using')