if __name__ == '__main__':
    N = int(input())
    arr = []
    a = 0
    b = 0
    for _ in range(N):
        command = input()
        command = command.split()
        if command[0] == "insert":
            a = int(command[1])
            b = int(command[2])
            arr.insert(a,b)
        elif command[0] == "print":
            print(arr)
        elif command[0] == "remove":
            a = int(command[1])
            arr.remove(a)
        elif command[0] == "append":
            a = int(command[1])
            arr.append(a)
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()