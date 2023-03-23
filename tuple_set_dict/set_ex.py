a={2,1,4,5}
b={2,5,1,2,5,1,2,1,2,3,5,1,2,3,5,2,1,5,2,5} #it removes all the duplixcate elements of the sets
print(a)
print(b)

#list to set
c=[1,5,3,2,1,21,12,2,5,1,2,2,5]
cs=set(c)
print(c)
print(cs)
print(type(c))
print(type(cs))

#empty set 
d= set()
print(d)
d.add('Appleseed')
d.add('Banana')
d.add('Pine apple')
d.add('Custurd Apple')
d.add('Apple')
print(d)
d.discard('Apple') #the better way to remove an item
print(d)
d.remove('Banana') #the dangerous way to remove and item
print(d)
d.clear()
print(d)