if __name__ == '__main__':
    n = int(input())

    integer_list = map(int, input().split())

    list_tupple = tuple((integer_list))
    print(hash(list_tupple))