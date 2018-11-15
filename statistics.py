from beggar import beggar

def statistics(Nplayers, games):
    """
    Works out the shortest, average and longest length from a number of games  

    The parameters take are:
        Nplayers - an integer which holds the number of players in the game
        games - an integer which holds how many games should be run

    Returns the shortest, average, and longest length games
    """
    
    # initialising the values
    # shortest is set to a very high value so the next number will replace it
    shortest = 9999999
    average = 0
    longest = 0
    totalTurns = 0

    # makes a deck of cards to be tested
    cardDeck = []
    for i in range(4):
        for j in range(2, 15):
            cardDeck.append(j)

    for i in range(games):
        # numnber of turns for the game to finish stored in currentGameTurns
        currentGameTurns = beggar(Nplayers, cardDeck, False)

        # finds and stores the longest length game
        if currentGameTurns > longest:
            longest = currentGameTurns
        
        # finds and stores the shortest length game
        if currentGameTurns < shortest:
            shortest = currentGameTurns

        # records the total number of turns
        totalTurns = totalTurns + currentGameTurns
    
    # calculates the average number of games
    average = totalTurns / games

    return shortest, average, longest


if __name__ == "__main__":
# runs the game for 2 to 10 players with 100 turns in each
    for numPlayers in range(2, 11):
        shortest, average, longest = statistics(numPlayers, 100)
        print('For', numPlayers, 'players')
        print('Shortest game:', shortest)
        print('Longest game:', longest)
        print('Average game:', average)
        print()
