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


if __name__ == "__main__":
    print(riffle(list(range(22)), 30))