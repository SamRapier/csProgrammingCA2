def riffle_once(L):
    import random

    halfList1 = L[:int(len(L)/2)]
    halfList2 = L[int(len(L)/2):]

    finalList = []

    for x in range(len(halfList1)):
        rInt = random.randint(0, 1)
        if rInt == 0:
            finalList.append(halfList1[x])
            finalList.append(halfList2[x])
        else:
            finalList.append(halfList2[x])
            finalList.append(halfList1[x])
    
    return finalList

def riffle(L, N):
    for i in range(N):
        L = riffle_once(L)
    
    return L

def quality(L):
    qualityCount = 0

    for count in range(len(L) - 1):
        if(L[count + 1] > L[count]):
            qualityCount = qualityCount + 1
    
    qualityScore = qualityCount / (len(L)-1)
    # print(qualityCount)
    return qualityScore

def average_quality(N, trials):
    testList = list(range(50))
    totalQuality = 0
    averageQuality = 0
    for i in range(trials):
        totalQuality = totalQuality + quality(riffle(testList, N))

    averageQuality = totalQuality / trials
    print(averageQuality)





if __name__ == "__main__":
    # print(riffle(list(range(22)), 30))
    # print(quality(list(range(50))))
    print(quality(riffle(list(range(50)), 30)))
    # names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu']
    # print(riffle_once(names))

    average_quality(2, 30)