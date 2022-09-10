#Write a python script to print first N natural numbers in reverse order
num=int(input())
r=range(num,0,-1)
for n in r:
    print(n,end=' ')