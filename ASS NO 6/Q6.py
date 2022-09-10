#Write a python script to check whether a given number is a three digit number or not.
a=int(input("Enter a no. ==> "))
if (a%1000==a and a//100!=0): 
    print("Yes") 
else:
    print("NO")