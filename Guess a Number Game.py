import random
computerinput=random.randint(0, 10)
#print(computerinput)
userinput=11 #because userinput cannot equal computerinput below
print(userinput)
while userinput!=computerinput:
    userinput = int(input('Enter a number(0-10): ')) #this must be included in the while loop
    if userinput == computerinput:
        print('Success')
    elif userinput > computerinput:
        print('Your guess is too high, try again!')
    else:
        print('Your guess is too low, try again!')