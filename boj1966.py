def q_sel(doc_important) :
    for doc_cur in doc_important :
        if doc_cur != max(doc_important) :
            pass
        else :
            doc_important.remove(doc_cur)
            

case = int(input())

for i in range(case) :
    step = 0
    N, M = map(int, input().split())
    doc_important = list(map(int, input().split()))
    print(step)