x= [] #empty list
#append, extend , insert methods
x.append(5)
x.append(1)
print(x)
x.append(10)
print(x)
for i in range (10,17):
    x.append(i)
print(x)
y=[23,54,45]
x.append(y)
print(x)
x.extend(y)
print(x)
x.insert(2,7)
print(x)
x.insert(7,'Hello') #string inserted at index 7
print(x)
x.insert(16,[1,2,3,4]) #string inserted at index 16
print(x)