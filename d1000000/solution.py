import sys

sys.stdin = open("input.txt")
testCases = int(input())

for testCase in range(1, testCases + 1):
    n = int(input())
    dice = [int(x) for x in input().split()]
    dice.sort()

    maxL = 0
    need = 1

    for i in range(n):
        die = dice[i]
        if die >= need:
            # take the die
            need += 1
            maxL += 1

    print("Case #" + str(testCase) + ": " + str(maxL))
