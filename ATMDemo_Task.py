import datetime
currentDate = datetime.date.today()
data = {
    'nico': 'nicopass',
    'paul': 'paulpass',
    'chris': 'chrispass',
    'mbah': 'mbahpass',
}


def register():
    list = []
    name = input('please enter username')
    name = name.capitalize()
    if name in data:
        print('username exist!')
        print('please try another user name')
        register()
    else:
        password = input('please enter password')
        #new = f'{name}:{password}'.split(':')
        list.append(name)
        list.append(password)
        data[list[0]] = list[1]
        print('sucessfully registered you can login to perform operations')
        login()


def login():
    name = input('enter your username\n')
    password = input('enter your password to your username\n')

    if (name in data and password == data[name]):
        print('welcome  %s\n' %name)
        print(currentDate.strftime('%d %b, %Y\n'))
        firstName = name[:3].upper()
        ac = str(id(name))
        number = '100003'
        accountNumber = number+ac+firstName
        print('your ACCOUNT NUMBER is {}\n'.format(accountNumber))
        return True
    else:
        print('your username or password do not match please try again')
        print('PLEASE ENTER VALID USERNAME AND PASSWORD!')
        login()
        return True

# 139997629232432

def logout():
    print('Are you Sure you want to logout of this account')
    logout = input("enter 'yes' to comfirm logout or 'cancel' to remain signin\n")
    if logout.lower() == 'yes':
        print('you have successfully to logout\n\n')

    elif logout == 'cancel':
        operation()



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
                print('YOU MAY WANT TO PERFORM ANOTHER OPERATION\n')
                operation()


            elif option == 2:
                deposit = int(input('how much will you like to deposit?\n'))
                print(f'successfully {deposit} into accountbalance is\n\n')
                print('YOU MAY WANT TO PERFORM ANOTHER OPERATION\n')
                operation()

            elif option == 3:
                complaint = input('what issue will you like to report?')
                print('thank you for contacting us\n\n')
                print('YOU MAY WANT TO PERFORM ANOTHER OPERATION\n')
                operation()

            elif option == 4:
                logout()

            else:
                print('invalid input ')
                print('please enter either 1, 2, or 3 to perform operation on your account')

    except ValueError:
        print('error please enter an interger type number')


print('welcome to ATM machine \n')
print('login if tou already have an account or register yourself\n')
try:
    option = int(input('please enter 1 to login or 2 to register\n'))

    if option ==1:
        isLoggedIn = False
        while isLoggedIn == False:
             isLoggedIn = login()

        if isLoggedIn == True:
          operation()
    elif option == 2:
        register()
except ValueError:
    print('enter either 1 or 2')