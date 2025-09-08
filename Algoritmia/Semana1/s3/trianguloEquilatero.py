stickLengths = list(map(int, input().split()))

stickLengths.sort()

if stickLengths[0] == stickLengths[2] or stickLengths[1] == stickLengths[3]:
    print(1)
else:
    print(0)