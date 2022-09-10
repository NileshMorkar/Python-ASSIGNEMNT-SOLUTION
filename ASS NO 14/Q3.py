'''Write a Python script to create a list of first N even natural numbers.
'''
num=int(input())
r=range(2,2*num+1,2)
A=[]
for n in r:
    A.append(n)
print(A)