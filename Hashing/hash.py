def mod(numbers,cellNumber):
    return numbers % cellNumber


def modeASCII(string,cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber    




print(modeASCII('ADITYA',20))