#################################################################################
#Diarmuid Whelan
#Exercise 1
# A program that displays Fibonacci numbers.
#D+D =8 PROGRAM WILL DISPLAY 8TH FIBONACCI NUMBER 
###################################################################################

def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



# Test the function with the following value.

x = 8

ans = fib(x)

print("Fibonacci number", x, "is", ans)





######################################################################################################
# Diarmuid Whelan
#Exercise 2
# A program that displays Fibonacci numbers using people's names.
##########################################################################################################


def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



name = "Whelan"

first = name[0]

last = name[-1]

firstno = ord(first)

lastno = ord(last)

x = firstno + lastno



ans = fib(x)

print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)


######################################################################################################################################
#Answers in Discussion Forums
#Exercise 1
#My name is Diarmuid, the first and last letter of my name (D + D = 4 + 4) give the number 8.  8th Fibonacci number is 21

#Exercise 2
#My surname is Whelan
#The first letter W is number 87
#The last letter n is number 110
#Fibonacci number 197 is 66233869353085486281758142155705206899077

#A computer understands only bits and bytes. 
#The characters we type in or feed into it are really encoded as bits.
# We interpret these bits as some numbers that represent those characters we fed. 
# These are what we call ASCII codes. ORD() gives the ASCII code of the character.
######################################################################################################################################
