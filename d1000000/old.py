import sys

sys.stdin = open("input.txt")
testCases = int(input())

for testCase in range(1, testCases + 1):
    print("----------------------------")
    n = int(input())
    dice = [int(x) for x in input().split()]
    dice.sort()

    pLeft = 0
    pRight = 0
    prev = 0
    maxL = 0

    for i in range(n):
        die = dice[i]
        if die > prev:
            print("INCREASING")
            # increasing, can use the next die no matter what (I think)
            pRight += 1
            prev = die
            print("die is: " + str(die) + ", maxL is: " + str(maxL) + ", prev is: " + str(prev) + ", pLeft is: " + str(pLeft) + ", pRight is: " + str(pRight) + ", i is: " + str(i))
        elif die == prev:
            # equal, can only use the next die if it is >= i
            if die > i:
                print("EQUAL IN THE CLEAR")
                pRight += 1
                prev = die
                print("die is: " + str(die) + ", maxL is: " + str(maxL) + ", prev is: " + str(prev) + ", pLeft is: " + str(pLeft) + ", pRight is: " + str(pRight) + ", i is: " + str(i))
            else:
                print("EQUAL, NEED TO ADJUST")
                print("diff is: " + str(pRight - pLeft) + " and maxL is: " + str(maxL))
                # equal, but the next die is less than i and doesn't have enough sides
                # move the left pivot up, set this as the max length found so far, and continue with accepting the next one
                if (pRight - pLeft) > maxL:
                    maxL = pRight - pLeft
                pLeft += 1
                pRight += 1
                prev = die
                print("die is: " + str(die) + ", maxL is: " + str(maxL) + ", prev is: " + str(prev) + ", pLeft is: " + str(pLeft) + ", pRight is: " + str(pRight) + ", i is: " + str(i))
    
    if (pRight - pLeft) > maxL:
        maxL = pRight - pLeft

    print("Case #" + str(testCase) + ": " + str(maxL))
