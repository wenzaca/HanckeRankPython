class Validator:
    def __init__(self, string):
        isalnum(string)
        isalpha(string)
        isdigit(string)
        islower(string)
        isupper(string)

def isalnum(string):
    for char in list(string):
        if str(char).isalnum():
            b = "True"
            break
        else:
            b = "False"
    print(b)

def isalpha(string):
    for char in list(string):
        if str(char).isalpha():
            b = "True"
            break
        else:
            b = "False"
    print(b)

def isdigit(string):
    for char in list(string):
        if str(char).isdigit():
            b = "True"
            break
        else:
            b = "False"
    print(b)

def islower(string):
    for char in list(string):
        if str(char).islower():
            b = "True"
            break
        else:
            b = "False"
    print(b)

def isupper(string):
    for char in list(string):
        if str(char).isupper():
            b = "True"
            break
        else:
            b = "False"
    print(b)

if __name__ == '__main__':
    s = input()
    Validator(s)
