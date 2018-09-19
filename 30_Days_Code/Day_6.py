if __name__ == '__main__':
    stringList = []

    for _ in range(int(input())):
        string = str(input())
        even = True
        resultEven = ''
        resultOdd = ''
        for char in string:
            if even:
                resultEven += char
                even = False
            else:
                resultOdd += char
                even = True
        print('%s %s' % (resultEven, resultOdd))