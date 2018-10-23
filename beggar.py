def beggar(Nplayers, deck, talkative = False):
    """
    Play a single game of beggar-your-neighbour

    The arguments taken are:
        -Nplayers (the number of players in the game)
        -deck (the shuffled deck of cards)
        -talkative (prints details of what is happening in the game)

    The function returns how many turns it takes to finish the game
    """

    from random import shuffle

    shuffle(deck)
    players = []
    pile = []
    count = 0

    for i in range(Nplayers):
        players.append([])

    for i in deck:
        players[count].append(i)
        count = count + 1
        if count >= Nplayers:
            count = 0



    count = 0
    turn = 0
    while not finished(players):
        if len(players[count]) > 0:
            turn = turn + 1
            if talkative == True:
                print(turn)
                print('Pile:    ', pile)

                for i in range(Nplayers):
                    print(i, players[i])
                
                print()
                            

            players[count], pile, reward = take_turn(players[count], pile)

            for i in reward:
                players[count - 1].append(i)

        count = count + 1
        if count >= Nplayers:
            count = 0
    


def take_turn(player, pile):
    """
    
    The arguments taken are:
        -player (takes the cards held by the current player)
        -pile (the current pile of cards)

    The funciton returns the players cards after the turn, the pile after the
    turn and th reward, the cards that should be given to the previous player
    if a penalty cards was played
    """

    highCards = [11, 12, 13, 14]

    if len(pile) > 0 and pile[-1] in highCards:
        penalty = pile[-1] - 10

        for i in range(penalty):
            card = player.pop(0)

            if card in highCards:
                break
            
            pile.append(card)

        reward = pile
        pile = []

    else:
        card = player.pop(0)
        pile.append(card)
        reward = []

    return player, pile, reward


def finished(players):
    # return true if one players has all the cards and the others have none

    return False


cardDeck = []
for i in range(4):
    for j in range(2, 15):
        cardDeck.append(j)

beggar(4, cardDeck, True)
