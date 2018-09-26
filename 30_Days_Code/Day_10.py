if __name__ == '__main__':
    n = str(bin(int(input())))
    n = n.replace("0b","")
    result = 0
    arr_result =[]
    for i in n:
        if int(i) == 1:
            result += 1
        else:
            result = 0
        arr_result.append(result)
    arr_result.sort(reverse=True)
    print(arr_result[0])
