if __name__ == '__main__':
    n = int(input())
    counter = 0
    maps = {}
    while counter<n:
        strings = str(input())
        maps[strings.split(" ")[0]] = strings.split(" ")[1]
        counter+=1
    counter = 0
    while counter<n:
        key = str(input())
        value = maps.get(key,"Not found")
        if value== "Not found":
            print(value)
        else:
            print(key+"="+value)
        counter+=1




