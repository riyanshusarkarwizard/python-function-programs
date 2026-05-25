# write a function in python to Check if a password:
#Has at least 8 characters
#Contains a digit
#Contains an uppercase letter


def check(password):
    if len(password) < 8:
        return "Weak Password"
    digit = False
    upper = False
    for ch in password:
        if ch.isdigit():
            digit = True
        if ch.isupper():
            upper = True
    if digit and upper:
        return "Strong Password"
    return "Medium Password"
p= input("Enter Password: ")
print(check(p))
