def riffle_once(L):
    """
    Performs a single riffle shuffle on a list

    Takes a list as a parameter

    Returns a shuffled list
    """
    import random

    # Initialise the two halves of the list and final list
    halfList1 = L[:int(len(L)/2)]
    halfList2 = L[int(len(L)/2):]

    finalList = []

    # loops through and creates a random number to determine which element is 
    # added first
    for x in range(len(halfList1)):
        rInt = random.randint(0, 1)
        
        if rInt == 0:
            # element from the first list is added to the final list first
            finalList.append(halfList1[x])
            finalList.append(halfList2[x])
        else:
            # otherwise, the element from the second list is added first
            finalList.append(halfList2[x])
            finalList.append(halfList1[x])
    
    return finalList

def riffle(L, N):
    """
    Shuffles a list multiple times

    The parameters are:
        A list which is to be shuffled
        A number which defines how many times the list should be shuffled

    This function returns the shuffled list
    """

    for i in range(N):
        L = riffle_once(L)


    return L

def check_shuffle():
    numsList = list(range(1, 21))

    names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu']

    assert len(numsList) == len(riffle(numsList, 2)), "The original list is not the same length as the shuffled list"
    assert len(names) == len(riffle(names, 2)), "The original list is not the same length as the shuffled list"



def quality(L):
    """ 
    This function determines the shuffled a list is

    The single parameter is a list

    The function returns a real number which represents the quality of the shuffled list 
    """
    qualityCount = 0

    for count in range(len(L) - 1):
        # loops through list and check if next item in the list is greater than the current item
        if(L[count + 1] > L[count]):
            qualityCount = qualityCount + 1
    
    qualityScore = qualityCount / (len(L)-1)
    
    # A good qualityScore is 0.5
    return qualityScore

def average_quality(N, trials):
    """
    Determines the average quality of a certain number of lists with a certain number of shuffles

    The parameters taken are:
        N - the number of shuffles when riffle is called
        trials - the number of lists which are analysed 
    
    The function prints out the average quality
    """

    # initialising values
    testList = list(range(50))
    totalQuality = 0
    averageQuality = 0

    # for every trial, the program, checks the quality of each shuffled list 
    # and adds it to a total quality variable
    for i in range(trials):
        totalQuality = totalQuality + quality(riffle(testList, N))

    # the average quality is calculated
    averageQuality = totalQuality / trials
    
    return averageQuality


if __name__ == "__main__":

    check_shuffle()

    print(riffle(range(1, 21), 2))

    names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu']
    print(riffle(names, 2))

    for N in range(1, 16):
        avgQual = average_quality(N, 30)
        print('After', N, 'shuffles, the average quality is', avgQual)

