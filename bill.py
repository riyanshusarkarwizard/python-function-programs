#Write a Python program using functions to calculate the electricity bill:
#First 100 units → ₹5/unit
#Next 100 units → ₹7/unit
#Above 200 units → ₹10/unit


def bill(a):
    if a<=100:
        b=a*5
    elif a>100 and a<=100:
        b=100*5+(a-100)*7
    else:
        b=100*5+100*7+(a-200)*10
    return b
u=float(input("PLEASE ENTER THE NUMBER OF UNITS CONSUMED::   "))
h=bill(u)
print("THE ELECTRICITY BILL TO BE PAID::  ",h)
