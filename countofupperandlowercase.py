#write a function to count the uppercase and lowercase letters in a sentence.


def countupper(x):
    u=0
    l=0
    if c in x:
        if c.isupper():
            u=u+1
        elif c.islower():
            l=l+1
    print("the number of uppercase letters are:   ",u)
    print("the number of lowercase letters are:    ",l)
h=input("PLEASE ENTER THE SENTENCE::   ")
countupper(h)
