N = int(input())

series = 665
nums = list()

while True :
    series += 1
    if '666' in str(series) :
        nums.append(series)
    
    if len(nums) == N:
        break

print(nums[-1])