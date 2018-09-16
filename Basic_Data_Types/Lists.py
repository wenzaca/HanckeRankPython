if __name__ == '__main__':
    N = int(input())
    final_list = []
    i=0
    while (i != N):
        command = input()
        commands = command.split(" ")
        if commands[0] == "insert":
            final_list.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            print(final_list)
        elif commands[0] == "remove":
            final_list.remove(int(commands[1]))
        elif commands[0] == "append":
            final_list.append(int(commands[1]))
        elif commands[0] == "sort":
            final_list.sort()
        elif commands[0] == "pop":
            final_list.pop()
        elif commands[0] == "reverse":
            final_list.reverse()
        else:
            print("command not known")
        i += 1