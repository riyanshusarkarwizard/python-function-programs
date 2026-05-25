#Write a function to calculate total, percentage, and grade.
#A → 90+
#B → 75–89
#C → 50–74
#Fail → Below 50


def grade (a,b,c,d,e):
    t=a+b+c+d+e
    p=t/5
    if p>=90:
        g="A"
    elif  p>=75 and p<=89:
        g="B"
    elif p>=50 and p<=74:
        g="C"
    else:
        g="D"
    return t,p,g
w=float(input("ENTER THE MARKS OF 1ST SUBJECT::   "))
x=float(input("ENTER THE MARKS OF 2ND SUBJECT::  "))
y=float(input("ENTER THE MARKS OF 3RD SUBJECT::  "))
z=float(input("ENTER THE MARKS OF 4TH SUBJECT::  "))
f=float(input("ENTER THE MARKS OF 5TH SUBJECT::  "))
t1,p1,g1=grade(w,x,y,z,f)
print("THE TOTAL MARKS OBTAINED IS::   ",t1)
print("THE PERCENTAGE OBTAINED IS::   ",p1)
print("THE GRADE OBTAINED IS::    ",g1)
