#write a program to define a function ispal(x) that will return true if x is palindrome else returns false.


def ispal(x):
    s=0
    m=x
    while x>0:
        d=x%10
        s=s*10+d
        x=x//10
    if m==s:
        return True
    else:
        return False
c=int(input("PLEASE ENTER THE NUMBER::  "))
if ispal(c)== True:
    print(c,"is a palindrome number...    ")
else:
    print(c,"is not aa palindrome number....     ")
    
