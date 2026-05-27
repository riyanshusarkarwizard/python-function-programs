#write a function to find the sum of the odd and the even digits separately in a number

def sumodd(x):
    o=0
    e=0
    for i in x:
        if i%2==0:
            e=e+i
        else:
            o=o+i
    print("the sum of odd digits is::   ",o)
    print("the sum of even digits is::  ",e)
y=list(input("please enter the list::    "))
sumodd(y)
