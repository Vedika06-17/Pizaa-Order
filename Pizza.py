print("Welcome to Python pizza delieveries")
size=input("What size do you want?s,m or l:").upper()
pepperoni=input("Do you want extra peppironi y or n: ").upper()
extra_cheese=input("Do you want extra cheese y or n: ").upper()
bill=0
if size=='S':
    bill=15
elif size=='M':
    bill=20
elif size=='L':
    bill=25
#How much to add to their bill based on their pepperoni choice
if pepperoni=='Y':
    if size=='S':
        bill+=2
    if size=='M':
        bill+=3
    if size=='L':
        bill+=4
#work out their final amount based on whwther if they want extra cheese or not
if extra_cheese=='Y':
    bill+=1
print(f"Your final bill is:Rs{bill}")