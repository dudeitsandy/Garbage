password = ''
while password != 'python123':
    password=input("enter password:")
    if password == 'python123':
        print('you are logged in')
    else:
        print('please enter correct user or password')
