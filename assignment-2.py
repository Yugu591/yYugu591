choice = input('''
Please select the type of operation you want to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
// for modular division
''')

num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))

choice1=num_1+num_2
choice2=num_1-num_2
choice3=num_1*num_2
choice4=num_1/num_2
choice5=num_1%num_2
if choice=='+':
    print("Addition:",choice1)
if choice=='-':
    print("Subtraction:",choice2)
if choice=='*':
    print("multiplication:",choice3)
if choice=='/':
    print("Divison:",choice4)    
if choice=='//':
    print("Modular division:",choice5)
# r+ and w+
# r+:
# it is used for openning a file and places the pointer at the beggining of the file to read..
# if the file is not present while we are openning then it will throw an exception..
# we cannot able to overwrite the content of a file in r+ mode
# w+:
#  it is also used for openning of a file and it delete the entire content present in the file and start from the beggining..
#  if the file is not present,then it will create a new file
#  it can be used for both reading and writting of a file
