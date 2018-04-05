#################################################################################
#GMIT Scripting and Programming
#Diarmuid Whelan, 2018-02-25
#Euler Problem 5
#################################################################################

smallest_num = 1
for i in range (1,21):
    if smallest_num % i > 0: # If the number is not divisible by i
        for k in range (1,21):
            if (smallest_num * k) % i == 0: # Find the smallest number divisible by i    
                smallest_num = smallest_num * k
                break
print ('Smallest number divisible by 1 to 20 inclusive: ', smallest_num)
