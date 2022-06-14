import sys

sys.stdin = open("input.txt")
testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().split()
    r = int(line[0])
    c = int(line[1])
    print("Case #" + str(testCase) + ":")

    for row in range(0,2 * r + 1):
        if row == 0:
            print(".." + "+-" * (c-1) + "+")
        elif row == 1:
            print(".." + "|." * (c-1) + "|")
        elif row % 2 == 0:
            print("+-" * c + "+")
        else:
            print("|." * c + "|")


