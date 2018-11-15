from random import shuffle

def beggar(Nplayers, deck, talkative = False):
    """
    Play a single game of beggar-your-neighbour

    The arguments taken are:
        -Nplayers (the number of players in the game)
        -deck (the shuffled deck of cards)
        -talkative (prints details of what is happening in the game)

    The function returns how many turns it takes to finish the game
    """

    # validates Nplayers so it is an integer between 2 and 15
    if not isinstance(Nplayers, int) or Nplayers < 2 or Nplayers > 15:
        raise ValueError("invalid argument for number of players: ", Nplayers)


    # Shuffle the deck and initialise the variables
    shuffle(deck)
    players = []
    pile = []
    count = 0
    currentPlayer = 0
    turn = 0
    previousPlayer = None

    # Add a list inside the players list for each player
    for i in range(Nplayers):
        players.append([])

    # Deal out a the cards for each player in the deck
    for i in deck:
        players[count].append(i)
        count = count + 1
        if count >= Nplayers:
            count = 0


    # This is the main game loop and continues until the finished function 
    # returns true
    while not finished(players):
         # This conditional skips players who are out of the game
        if len(players[currentPlayer]) > 0:
            turn = turn + 1    

            # This print the details of the game
            if talkative == True:
                print('Turn:', turn)
                print('Pile:    ', pile)

                for i in range(Nplayers):
                    if i == currentPlayer:
                        print('*  ', i, '  ', players[i])
                    else:
                        print('   ', i, '  ', players[i])
                
                print()

            # Plays the next turn and saves the returned tuples
            players[currentPlayer], pile, reward = take_turn(players[currentPlayer], pile)

            # Add the reward to the previous player
            for i in reward:
                players[previousPlayer].append(i)

            # This ensures that players who are out of the game will not 
            # recieve a reward
            previousPlayer = currentPlayer

            
        # This increases the current player counter and ensures that it loops
        # back to the first person instead of out of range 
        currentPlayer = currentPlayer + 1
        if currentPlayer >= Nplayers:
            currentPlayer = 0
    
    # prints out the final hand in the game to show who won
    if finished(players):
        if talkative == True:
            print('Final hand')
            print('Pile:    ', pile)

            for i in range(Nplayers):
                print('   ', i, '  ', players[i])
            
            print('\nThere were', turn, 'turns in this game')

    return turn


def take_turn(player, pile):
    """
    This function is called for every turn in the game. It checked if a high 
    card is on the top of the pile and makes the next player pay the penalty. 
    It adds a card from the current players hand to the pile. 

    The arguments taken are:
        -player (takes the cards held by the current player)
        -pile (the current pile of cards)

    The funciton returns the players cards after the turn, the pile after the
    turn and the reward
    """

    # Defining the high cards
    highCards = [11, 12, 13, 14]

    # If the top card on the pile is a high cards, it gives a penalty to the 
    # current player. If that player draws a high card, they stop playing the 
    # penalty cards and moves on
    if len(pile) > 0 and pile[-1] in highCards:
        penalty = pile[-1] - 10
        newHigh = False

        # Payer pays the penalty, if they run out of cards while paying they 
        # are out
        for i in range(penalty):
            
            if len(player) > 0:
                card = player.pop(0)

                pile.append(card)

                if card in highCards:
                    newHigh = True
                    break
    
        # Setting the reward for the person who played the last high card
        if newHigh == False:
            reward = pile
            pile = []
        else:
            reward = []

    else:
        # When no high card is played the players top card is 
        # added to the pile
        card = player.pop(0)
        pile.append(card)
        reward = []

    return player, pile, reward


def finished(players):
    """
    Return true if one player has all the cards and the others have none

    Checks to see if the game has finished by checking if the other players 
    any cards left

    The single argument taken is the players list
    """
    
    numOut = 0

    # loops through and checks how many players are out of the game
    for i in range(len(players)):

        if len(players[i]) == 0:
            numOut = numOut + 1

    
    # if there is only one player left, the function returns True
    if numOut == len(players) - 1:
        return True

    return False


if __name__ == "__main__":
    numPlayers = input('How many players are there? ')

    # Creates a deck of cards
    cardDeck = []
    for i in range(4):
        for j in range(2, 15):
            cardDeck.append(j)

    
    beggar(int(numPlayers), cardDeck, True)