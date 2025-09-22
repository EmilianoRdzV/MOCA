n = int(input())
sequenceOne = list(map(int, input().split()))
sequenceTwo = list(map(int, input().split()))

if sequenceOne == sequenceTwo:
    print(1)
else:
    print(0)