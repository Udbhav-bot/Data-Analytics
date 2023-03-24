#creating a dictionary
a={'Name':'Zara','Age':7,'Class':'First'}
print(a)

#getting all the keys from the dictionary
print(a.keys()) #use list (a.keys()) to display as list

#getting all the items from the dictionary as a list of typles
print(a.items())

#getting all the values from the dictionary
print(a.values())

#nested dict
b={
    'fruits':{'Apple':'1 kg', 'Cutard apple':'3kg'},
    'vegetables':{'potato':'5kg', 'tomato':'500g'},
    'cereals':{'rice':'1 kg', 'wheat':'3kg'},
}

from pprint import pp
pp(b)

#accessing a value from a dict
print(a['Name'])
print(b['fruits'])
# print(a['City']) #key error

#accessing a value from a dict using get()
print(a.get('Name'))
print(a.get('Class'))
print(a.get('City')) #none
print(a.get('City', 'Not found'))  #default values can be specified
print(a.get('Name','Not found')) #if the key is present it will show its value

#traversing a dict 
#style 1
for key in a:
    print(key,a[key]) #a[key] is for getting a value

#style 2
for key, value in a.items():
    print(key ,value)

#only values
for values in a.values():
    print(value)

#only keys 
for key in a.keys():
    print(key)