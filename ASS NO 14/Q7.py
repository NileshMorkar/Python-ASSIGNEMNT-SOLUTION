#Write a Python script to remove all non int values from a list.

A=[12,"Nil",12.3,True,56,89,23]
print(A)
i=0
#using While loop
while(i<len(A)):
    if(type(A[i])!=int):
        del A[i]
        i-=1
    i+=1
print(A)

#using for loop

B=[12,"Nil",12.3,True,56,89,23]
C=[]
print(B)
for n in B:
    if(type(n)==int):
        C.append(n)
B=C
print(B)