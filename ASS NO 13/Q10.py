'''Write a Python script to create a list, where each element of the list is a digit of a
given number.
'''

#store as string
num=input("Enter a no.== >")
A=[]
for n in num:
    A.append(n)
print(A)

# Store as integer
B=[]
num=int(input("ENter a no.== >"))
k=1
n=num//k %10
while (n!=0):
    k*=10
    B.append(n)
    n=num//k %10
print(B)