#Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter a year "))
if(year%400==0):
    print("\n",year,"is leap Year")
elif(year%100==0):    
    print("\n",year,"is NOT leap Year")
elif(year%4==0):
    print("\n",year,"is leap Year")
else:
    print("\n",year,"is NOT leap Year")