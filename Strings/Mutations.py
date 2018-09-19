def mutate_string(string, position, character):
    strings = list(string)
    strings[position] = str(character)
    return ''.join(strings)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)