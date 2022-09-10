'''11. Write a python script to take the month value in numeric format and display the
number of days in it.
'''

mon=int(input("Enter a month ==> "))
if(mon==2):
    print("29")
elif((mon%2 and mon<=7) or (mon %2==0 and mon>=8)):
    print("31")
else :
    print("30")