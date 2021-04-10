import datetime
import random



#database of existing user and passwords in a dictionary
currentDate = datetime.date.today()
data = {
    'nico': 'nicopass',
    'paul': 'paulpass',
    'chris': 'chrispass',
    'mbah': 'mbahpass',
}




#registration function
def register():
    list = []
    name = input('please enter username')
    if(name in data):
        print('username exist!')
        print('please try another user name')
        print('=============================================')
        register()
    else:
        password = input('please enter password')
        #new = f'{name}:{password}'.split(':')
        list.append(name)
        list.append(password)
        data[list[0]] = list[1]
        print('sucessfully registered you can login to perform operations')
        print(name.upper())
        print('===========================================================')
        login()





#login function
def login():
    name = input('enter your username\n')
    password = input('enter your password to your username\n')

    if (name in data and password == data[name]):
        print('welcome  %s\n' %name.upper())
        print(currentDate.strftime('%d %b, %Y\n'))

        #randomly generating account number using a standard 100003, a random number ending with a three later signature of username
        firstName = name[:3].upper()
        ac = random.randrange(341234567890, 2345678901, -2344678888)
        ac = str(ac)
        number = '100003'
        accountNumber = number+ac+firstName
        print('your ACCOUNT NUMBER is {}\n'.format(accountNumber))
        return True
    else:
        print('your username or password do not match please try again')
        print('PLEASE ENTER VALID USERNAME AND PASSWORD!')
        print('========================================================')
        login()
        return True



# logout opreation

def logout():
    print('Are you Sure you want to logout of this account')
    logout = input("enter 'yes' to comfirm logout or 'cancel' to remain signin\n")
    if logout.lower() == 'yes':
        print('you have successfully to logout\n\n')

    elif logout == 'cancel':
        operation()



def operation():
    print('select option you want to do in your account')
    print('=============================================')
    print('enter 1 to withdraw')
    print('=============================================')
    print('enter 2 to deposit')
    print('=============================================')
    print('enter 3 to complain')
    print('=============================================')
    print('enter 4 to logout\n')
    print('=============================================')

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
                print('========================================================')
                operation()

            elif option == 3:
                complaint = input('what issue will you like to report?')
                print('thank you for contacting us\n\n')
                print('YOU MAY WANT TO PERFORM ANOTHER OPERATION\n')
                print('========================================================')
                operation()

            elif option == 4:
                logout()

            else:
                print('invalid input ')
                print('please enter either 1, 2, or 3 to perform operation on your account')

    except ValueError:
        print('error please enter an interger type number\n')
        print('=============================================')
        operation()


print('welcome to ATM machine')
print('===========================================================\n')
print('login if tou already have an account or register yourself\n')
try:
    option = int(input('please enter 1 to login or 2 to register\n'))

    if option == 1:
        isLoggedIn = False
        if isLoggedIn == False:
            isLoggedIn = login()

        if isLoggedIn == True:
            operation()
    elif option == 2:
        register()

except:
    print('enter either 1 or 2 only to make your choice')