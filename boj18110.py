N = int(input())
slice_aver = 0
user_diff = list()

if N != 1:
    slice_aver = round(N * 15/100)

for i in range(N) :
    user_diff.append(int(input()))

user_diff.sort()

del user_diff[:slice_aver]
del user_diff[(-1 * slice_aver):]

aver_u = 0
for b in user_diff:
    aver_u += b

if len(user_diff) == 0:
    print(aver_u)
else :
    print(round(aver_u / len(user_diff)))
