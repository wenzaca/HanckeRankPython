if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort(key=int)
    lenght = len(arr)
    if lenght==1:
        print(arr[0])
    else:
        print(arr[lenght-2])