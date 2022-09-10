#Write a python script to sort a list.

num=int(input("Enter Size of List==> "))
A=[]
for i in range(num):
    A.append(int(input()))
A.sort()
print(A)