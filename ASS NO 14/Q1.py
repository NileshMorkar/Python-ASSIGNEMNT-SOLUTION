'''1. Write a Python script to create a list of first N natural numbers'''

num=int(input("Enter a no.==>"))
r=range(1,num+1)
A=[]
for n in r:
    A.append(n)
print(A)
