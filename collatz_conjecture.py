#Diarmuid Whelan 2018-02-10
#Collatz Conjecture Exercise
#https://en.wikipedia.org/wiki/Collatz_conjecture

n = 1992
while n >1:
    if n % 2 == 0:
        n=n/2
        print(n) 
    else:
        n=3*n+1
        print(n)
