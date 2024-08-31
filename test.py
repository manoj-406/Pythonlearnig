""" docstring"""
n = int(input())
for i in range (n):
    a , b = map(int,input().split())
    if b == 0:
        print(0)
    else:
        c = a // b
        f = c * b
        print (f)
# End-of-file (EOF)