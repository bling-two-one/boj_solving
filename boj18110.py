def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


N = int(input())
slice_aver = 0
user_diff = list()

if N != 1:
    slice_aver = roundUp(N * 15/100)
else :
    slice_aver = 0

for i in range(N) :
    user_diff.append(int(input()))

user_diff.sort()

del user_diff[:slice_aver+1]
del user_diff[(-1 * slice_aver):]

aver_u = 0
for b in user_diff:
    aver_u += b

print(round(aver_u / len(user_diff)))
