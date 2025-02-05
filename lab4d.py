#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Place code here - refer to function specifics in section below
    return s[:5]

def last_seven(s):
    # Place code here - refer to function specifics in section below
    return s[-7:]

def middle_number(n):
    # Place code here - refer to function specifics in section below
    n_str = str(n)
    return n_str[1:3]

def first_three_last_three(s1, s2):
    # Place code here - refer to function specifics in section below
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))                # Outputs 'Hello'
    print(first_five(str2))                # Outputs 'Senec'
    print(last_seven(str1))                # Outputs 'World!!'
    print(last_seven(str2))                # Outputs 'College'
    print(middle_number(num1))             # Outputs '50'
    print(middle_number(num2))             # Outputs '.5'
    print(first_three_last_three(str1, str2))  # Outputs 'Helege'
    print(first_three_last_three(str2, str1))  # Outputs 'Send!!'
