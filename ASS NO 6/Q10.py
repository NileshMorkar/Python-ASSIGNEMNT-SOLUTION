'''Write a python script to print greater among three numbers.
print number only once even if the numbers are the same.
'''
a,b,c=int(input("Enter Three no. ==>\n")),int(input()),int(input())
if(a>b):
    if(a>c):
        print("Greatest number==>",a)
    else:
        print("Greatest number==>",c)
else:
    if(b>c):
        print("Greatest number==>",b)
    else:
        print("Greatest number==>",c)
