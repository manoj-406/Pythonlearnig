'''This is a program to find weather the number is prime or not

def is_prime(number):
    for index in range(2, number):
        if number % index ==0:
            return False

    return True

def factorial(num):
    index = 0
    for i  in range(num+1):
        index += i * i 
        return index

num = 5
print(factorial(num))
'''
# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    x= 6 / a
    print(b * x)
  

