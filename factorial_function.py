###################################################################################
#GMIT Scripting and Programming
#Diarmuid Whelan, 2018-03-29
#Exercise 6 Factorial Function
#Write a Python script containing a function called factorial() that takes a single input/argument
#which is a positive integer and returns its factorial. The factorial of a number is that 
#number multiplied by all of the positive numbers less than it. For example, the factorial of 5
#is 5x4x3x2x1 which equals 120. You should, in your script, test the function by calling it 
#with the values 5, 7, and 10.
###################################################################################
def factorial(number):
    multiply=1
    for i in range(1,number+1):
        multiply=multiply*i
    return multiply    

print('The factorial of 5 is:', factorial(5))
print('The factorial of 5 is:', factorial(7))
print('The factorial of 5 is:', factorial(10))