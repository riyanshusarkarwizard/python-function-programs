#WRITE A FUNCTION TO COUNT THE NO OF WORDS IN A STRING


def words(y):
    w=y.split()
    d=len(w)
    print("THE  NUMBER OF WORDS IN THE STRING IS:::    ",d)
n=input("PLEASE ENTER THE STRING WHOSE NO. OF WORDS IS TO BE FOUND:::     ")
words(n)
