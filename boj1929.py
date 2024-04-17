def is_prime(N) :
    for i in range(2, N) :
        if N % i == 0 :
            return False
    return True


M, N = map(int, input().split())

for a in range(M, N+1) :
    if is_prime(a) == True :
        print(a)
