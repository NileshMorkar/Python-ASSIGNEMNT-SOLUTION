'''Write a python script to accept one complex number 
from the user and display the greater number between real 
part and imaginary part
'''
print("Enter a Complex no.==> ")
C=complex(input())
print( C.imag if C.imag>C.real else C.real)