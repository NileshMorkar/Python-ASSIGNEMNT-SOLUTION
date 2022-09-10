#Write a python script to print first N odd natural numbers
num=int(input())
r=range(1,2*num,2)
for n in r:
    print(n,end=' ')
