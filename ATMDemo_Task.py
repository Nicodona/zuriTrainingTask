data = {
    'nico': 'nicopass',
    'paul': 'paulpass',
    'chris': 'chrispass',
    'mbah': 'mbahpass',
}
def login():
    name = input('enter your username\n')
    password = input('enter your password to your username\n')

    if (name in data and password == data[name]):
        print('welcome Mr %s' %name)
        return True
    else:
        print('your username or password do not match please try again')
        return  False

def operation():
    print('select option you want to do in your account')
    print('enter 1 to withdraw')
    print('enter 2 to deposit')
    print('enter 3 to complain')
    print('enter 4 to logout\n')

    try:
            option = int(input('enter any option listed above\n'))

            if option == 1:
                withdraw = int(input('how much will you like to withdraw\n'))
                print(f'take your cash  {withdraw}\n\n')


            elif option == 2:
                deposit = int(input('how much will you like to deposit?\n'))
                print(f'successfully {deposit} into accountbalance is\n\n')

            elif option == 3:
                complaint = input('what issue will you like to report?')
                print('thank you for contacting us\n\n')

            elif option == 4:
                print('Are you Sure you want to logout of this account')
                logout = input("enter 'yes' to comfirm logout or 'cancel' to remain signin\n")
                if logout.lower() =='yes':
                    print('you have successfully to logout\n\n')
                    return login()

            else:
                print('invalid input ')
                print('please enter either 1, 2, or 3 to perform operation on your account')

    except ValueError:
        print('error please enter an interger type number')



isLoggedIn = False

if isLoggedIn == False:
  isLoggedIn = login()

while isLoggedIn == True:
  operation()
