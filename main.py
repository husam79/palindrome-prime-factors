########################################################################################################
### This program written by Husam Burhan based on code developed by Ibrahim Nakshabandi              ###
### This program will find each palindrome number which factorized into two palindrome prime factors ###
### You can set the final number to reach using the "final_number" variable"                         ###
########################################################################################################

import math

final_number = 3002004
result = []
counter = 0

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x % i == 0:
            return False
    
    return True

def is_palindrome(x):
    str_num = str(x)
    length = len(str_num)

    if length == 1:
        return True

    for i in range(length // 2):
        if str_num[i] != str_num[length - i - 1]:
            return False

    return True


for i in range(2,final_number):
    if(is_palindrome(i) and is_prime(i)):
        result.append(i)

for i in range(len(result) - 2):
    for t in range(i + 1, len(result)):
        num = result[i] * result[t]
        if is_palindrome(num):
            print(result[i]," * ", result[t], " = ", num)
            counter = counter + 1

print("The number of these numbers is: ", counter)
