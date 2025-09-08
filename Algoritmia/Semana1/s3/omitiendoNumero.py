n = int(input())
nums = list(map(int, input().split()))

maxVal = max(nums)
result = [num for num in nums if num != maxVal]

print(len(result))
if result:
    print(*result)
