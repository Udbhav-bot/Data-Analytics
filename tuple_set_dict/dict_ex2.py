contacts={
    'emergency':'112,',
    'office':'9875640321',
}
while True:
    print('->call📞')
    print('->add👤')
    print('->exit📞')
    cnt=input('Enter your choice: ')
    if cnt =='call':
        name=input ('Enter name of contact: ')
        if name in contacts:
            print(f'calling {name} at {contacts[name]}')
        else:
            print(f'{name} not found')
    elif cnt=='exit':
        break
    elif cnt=='add':
        name= input ('enter name of contact:')
        number=int(input ('Enter number'))
        contacts[name]= number
        print(f'{name} added successfully')
    else:
        print('invalid choice')
    print('-'*10)
    