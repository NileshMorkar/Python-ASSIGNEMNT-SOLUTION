'''Write a Python script to print indices of all occurrences of a given element in a given
list.'''
num=int(input("Enter Size of List==> "))
A=[]
for i in range(0,num):
    A.append(int(input()))
print(A)
n=int(input("Enter a no.==> "))
k=0
for i in range(0,num):
    if(n==A[i]):
        print(i)
        k=1
if(k!=1):
    print("Invalid Input")