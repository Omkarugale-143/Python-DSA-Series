def factorial(n):
    if n ==0 or n==1:
        return 1
    return n * factorial(n-1)

number = int(input("Enter the number"))
print(factorial(number))



def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(number))


def sum_n(n):
    if n==0:
        return 0
    return n + sum_n(n-1)

print(sum_n(number))

def Reverse_str(s):
    if len(s) == 0:
        return ""
    return s[-1] + Reverse_str(s[:-1])

name = input("Enter the string") 
print(Reverse_str(name))   


def power(a,b):
    if b == 0:
        return 1
    
    return a * power(a,b-1)

num1 = int(input("Enter the number for A"))
num2  =  int(input("Enter the number for B"))
print(power(num1,num2))


def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    return palindrome(s[:-1])

print(Reverse_str(name), "is palindrome")


def sum_digits(n):
    if n == 0:
        return 0
    return(n%10) + sum_digits(n//10)

print(sum_digits(124))