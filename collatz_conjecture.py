#################################################################################
##GMIT Scripting and Programming
#Diarmuid Whelan 2018-02-10
#Collatz Conjecture Exercise
#https://en.wikipedia.org/wiki/Collatz_conjecture
#Complete the exercise discussed in the Collatz conjecture video by writing a single Python script that 
#starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three 
#and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer
#should be printed to the screen.
#If you wish to enhance your program, have the program ask the user for the integer 
#instead of specifying a value at the start of your code.
#Will use 1992(year I was born) to test
#################################################################################


 
n=int(input("Please enter number:")) #Enter an integer
while n >1:    #continue until n=1
    if n % 2 == 0:  #if n is divisible evenly by 2 do so 
        n=n/2
        print(n) 
    else:
        n=3*n+1     #if n is not divisible by 2 multiply by 3 and add 1
        print(n)
