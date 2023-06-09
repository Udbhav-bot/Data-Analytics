msg= "Journey Before Destination"
msg_upr= msg.upper()
msg_lwr= msg.lower()
msg_cpt= msg.capitalize()
msg_title= msg.title()
msg_swp= msg.swapcase()
msg_cf= msg.casefold()

print(msg)
print(msg_upr)
print(msg_lwr)
print(msg_cpt)
print(msg_title)
print(msg_swp)
print(msg_cf)

#alignment
print(msg.ljust(100,'_'))
print(msg.rjust(100))
print(msg.center(100))

#aligment with f-strings or padding

print(f'{msg.rjust(50)}') #same as rjust
print(f'{msg:>50}') #same as rjust #it moves toward the pointed side
print(f'{msg:<50}') #same as ljust #it moves toward the pointed side
print(f'{msg:^50}') #same as center #it moves toward the pointed side
