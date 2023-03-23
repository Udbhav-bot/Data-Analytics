x=(1,2,3) #tuple 
y=2,5,2,1 #tuple packing
print(x)
print(y)
print(type(x))
print(type(y))
print(x[0]) #index0
print(x[1]) #index1
print(y[-1]) #index -1
z=(1,2,3,4,5,6,7,8,9,10)
print(z[:5]) #slicing

#tuple methods -count , index

a=('Apple','Apple','Apple','Banana','Pine apple','custard Apple')
print(f'len of a is {len(a)}')
print(f'Apple occurs {a.count("Apple")} times')
print(f'Pine apple occurs {a.count("Pine apple")}times')
print(f'Banana is at index {a.index("Banana")}')

#tuple to list
zl=list(z)
print(type (z), type(zl))
print(z,zl)
#single item tuple
s=(1,) #comma is important to make it a tuple
s2=2, #also tupple 
print(s,s2)
print(type(s))