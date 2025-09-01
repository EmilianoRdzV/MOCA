nums = list(map(int, input().split()))

sNums = sorted(nums)
misplaced = 0

if nums[0] != sNums[0]:
    misplaced += 1
if nums[1] != sNums[1]:
    misplaced += 1
if nums[2] != sNums[2]:
    misplaced += 1

if misplaced == 0:
    print(0)
elif misplaced == 2:
    print(1)
else:
    print(2)