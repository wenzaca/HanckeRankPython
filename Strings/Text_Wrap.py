import textwrap

def wrap(string, max_width):
    list_wrap = textwrap.wrap(string, max_width)
    result =''
    for i in list_wrap:
        result+=i+'\n'
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)