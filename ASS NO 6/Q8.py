'''Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
'''
print("Enter a,b,c of aX^2+bX+C ==> ")
a,b,c=int(input("Enter a  ==> ")),int(input("Enter b ==> ")),int(input("Enter c ==> "))
D=b**2-4*a*c
if(D>0):
    print("Distinct Roots")
elif(D==0):
    print("Real and Equal")
else:
    print("Imaginary Roots")