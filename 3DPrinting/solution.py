import sys

sys.stdin = open("input.txt")
testCases = int(input())

for testCase in range(1, testCases + 1):
    printer1 = [int(x) for x in input().split()] 
    printer2 = [int(x) for x in input().split()] 
    printer3 = [int(x) for x in input().split()]

    resc = -1
    resm = -1
    resy = -1
    resk = -1

    maxc = min(printer1[0], printer2[0], printer3[0])
    maxm = min(printer1[1], printer2[1], printer3[1])
    maxy = min(printer1[2], printer2[2], printer3[2])
    maxk = min(printer1[3], printer2[3], printer3[3])

    total = maxc + maxm + maxy + maxk
    diff = total - 10**6
#    print("total is: " + str(total))
#    print("diff is: " + str(diff))
    # diff is 750,000

    if diff < 0:
        print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
    elif diff == 0:
        print("Case #" + str(testCase) + ": " + str(maxc) + " " + str(maxm) + " " + str(maxy) + " " + str(maxk))
    else:
        # need to decrease to 10**6
        # maxc is 699508
        if maxc >= diff:
            resc = maxc - diff
            diff = 0
            print("Case #" + str(testCase) + ": " + str(resc) + " " + str(maxm) + " " + str(maxy) + " " + str(maxk))
        if maxc < diff:
#            print("resc is: " + str(resc))
#            print("diff is: " + str(diff))
#            print("maxc is: " + str(maxc))
            resc = 0
            diff -= maxc
#            print("diff is now: " + str(diff))
        if maxm >= diff and diff != 0:
            #print("got here")
            resm = maxm - diff
            print("Case #" + str(testCase) + ": " + str(resc) + " " + str(resm) + " " + str(maxy) + " " + str(maxk))
            diff = 0
        if maxm < diff:
            resm = 0
            diff -= maxm
        if maxy >= diff and diff != 0:
            resy = maxy - diff
            print("Case #" + str(testCase) + ": " + str(resc) + " " + str(resm) + " " + str(resy) + " " + str(maxk))
            diff = 0
        if maxy < diff:
            resy = 0
            diff -= maxy
        if maxk >= diff and diff != 0:
            resk = maxk - diff
            print("Case #" + str(testCase) + ": " + str(resc) + " " + str(resm) + " " + str(resy) + " " + str(resk))
            diff = 0
