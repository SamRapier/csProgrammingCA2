from beggar import beggar

def statistics(Nplayers, games):
    
    
    shortest = 9999999
    average = 0
    longest = 0
    totalTurns = 0

    cardDeck = []
    for i in range(4):
        for j in range(2, 15):
            cardDeck.append(j)

    for i in range(games):
        currentGameTurns = beggar(Nplayers, cardDeck, False)

        if currentGameTurns > longest:
            longest = currentGameTurns
        
        if currentGameTurns < shortest:
            shortest = currentGameTurns

        totalTurns = totalTurns + currentGameTurns
    
    average = totalTurns / games

    return shortest, average, longest


if __name__ == "__main__":
    for numPlayers in range(2, 11):
        shortest, average, longest = statistics(numPlayers, 5000)
        print('For', numPlayers, 'players')
        print('Shortest game:', shortest)
        print('Longest game:', longest)
        print('Average game:', average)
        print()

    # shortest, average, longest = statistics(2, 10)
    # print('Shortest game:', shortest)
    # print('Longest game:', longest)
    # print('Average game:', average)
    # print()