name='Udbhav Dwivedi'
fname=name[:6]
lname=name[7:]
print(fname)
print(lname)
revname=name[::-1]
print(revname)
evenname=name[1::2]
print(evenname)
oddname=name[0::2]
print(oddname)

message='''The New Mexico Territory was an organized incorporated
territory of the United States from September 
9, 1850, until January 6, 1912. The territory 
was created from the U.S. provisional government 
of New Mexico, a result of Santa Fe de Nuevo 
México becoming part of the American frontier 
after the Treaty of Guadalupe Hidalgo. 
It existed with varying boundaries until the 
territory was admitted to the Union as the state 
of New Mexico. This illustration, created by 
Henry Mitchell for State Arms of the Union, 
published by Louis Prang in 1876, depicts the territory's 
coat of arms, adopted by legislation in 1887: "The coat of arms of 
the territory of New Mexico shall be the Mexican Eagle grasping a
serpent in its beak, the cactus in its talons, shielded by the
American eagle with outspread wings, and grasping arrows in its 
talons.
'''
print(f'length of message is ,{len(message)}')
#first 100 character
print(message[:101])
#last 200 character
print(message[648:])
print(message[-200:])
#every 10 character
print(message[0::10])
#all data except first 100 and last 100
print(message[100:-100])