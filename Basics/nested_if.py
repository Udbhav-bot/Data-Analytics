username= input ('Enter Username: ')
email= input('Enter email: ')
pwd= input('Enter password: ')
cpwd= input('Confirm password: ')

if len (username) > 0 and username.isalnum():
    if len(email)>0 and '@' in email:
        if len(pwd) >= 4:
            if pwd == cpwd:
                print ('Registration successfull')
            else:
                print('Password do not match')
        else:
            print('length of password is short')
    else:
        print('Invalid email')
else:
    print('Username is invalid')