'''Write a Python script to print distinct elements 
along with their frequencies of occurrence in the list.
'''

A=[11,2,5,6,2,5,11,10,3,5]
print(A)
for n in A:
    print(n,"==>",A.count(n))

#to print only one time...
B=[3,5,2,6,2,5,5,3,6,5]
print(B)
i=min(B)
while(i<=max(B)):
    j=0
    k=0
    while(j<10):
        if(i==B[j]):
            k+=1
        j+=1
    if (k!=0):
        print(i,"==>",k)
    i+=1
