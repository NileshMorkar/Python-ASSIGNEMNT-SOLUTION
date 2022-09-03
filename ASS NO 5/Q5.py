'''Write a python script which takes a three digit number from the user and displays
only its first digit.
'''
num=int(input("Enter a number ==> "))
print((num//100)%10)