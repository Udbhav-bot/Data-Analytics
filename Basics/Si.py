p = int (input (' Enter Principal Amount-> '))
r = int (input (' Enter Interest Rate-> '))
t = int (input (' enter time in years-> '))
si = (p*r*t)/ 100
ra= si + p
print('Simple Interest', si)
print('Returning Amount', ra)