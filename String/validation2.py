a= input ('Enter a Number: ')
b= input ('Enter another Number: ')
if a.isnumeric() and b.isnumeric():
    a,b=int(a),int(b)
    c=a+b
    print('The sum of the numbers is:',c)
else:
    print('Please enter numbers only')