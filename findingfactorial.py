# factorial finder
# finding factorial of any number easily
# Code ><

num = int(input('Enter the number: '))
factorial = 1

if num==0:
    print("The factorial of 0 is 1.")
elif num<0:
    print("Sorry, no negative number exist in factorial.")
else:
    for i in range(1, num+1):
        factorial = factorial*i
print("The factorial of",num,"is",factorial)