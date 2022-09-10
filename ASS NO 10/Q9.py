#Write a python script to print cubes of first N natural numbers
num=int(input())
r=range(1,num+1)
for n in r:
    print(n**3,end=' ')