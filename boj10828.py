import sys

def push(X,stack=list()) :
    stack.insert(0, X)

N = int(input())
L = list()

for i in range(N) :
    command = sys.stdin.readline().rstrip()
    if 'push' in command :
        push(int(command[-1]), L)

    elif command == 'pop' :
        if len(L) > 0 :
            print(L.pop(0))
        else :
            print(-1)

    elif command == 'size' :
        print(len(L))

    elif command == 'empty' :
        if len(L) == 0:
            print(1)
        else :
            print(0)

    elif command == 'top' :
        if len(L) == 0:
            print(-1)
        else :
            print(L[0])