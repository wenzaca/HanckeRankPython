if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print("Weird")
    elif N <= 5 and N>= 2:
        print("Not Weird")
    elif N>5 and N<21:
        print("Weird")
    elif N>20:
        print("Not Weird")