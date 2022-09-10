#Write a python script to print first N odd natural numbers in reverse order
num=int(input())
r=range(2*num-1,0,-2)
for n in r:
    print(n,end=' ')
