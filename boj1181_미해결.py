N = int(input())
text_lists = []

T = []

for i in range(N) :
    T.append(input())

T = list(set(T))
T.sort(key=len)

for a in range(51) :
    temp_lists = []
    for t in T :
        if len(t) == 

print(T)
