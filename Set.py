import random
from random import shuffle

def main():
    # Creating the deck
    deck = createdeck()

    # Shuffling the deck
    shuffle(deck)

    # Dealing out starting cards
    table = deck[:12]
    deck = [i for i in deck if i not in table]
    for card in table:
        print(card)

    # Searching for a set
    Set = False
    while(Set == False):
        for card1 in table:
            for card2 in table:
                for card3 in table:
                    if card1 != card2 != card3:
                        if detectset(card1, card2, card3) == True:
                            print('AAI')
                            Set = True
                            
                
        


def detectset(card1, card2, card3):

    for i in range(3):
        if card1[i] == card2[i] == card3[i] or card1[i] != card2[i] != card3[i]:
            Set = True
        else:
            return False

    if Set == True:
        return True


def createdeck():
    color = -1
    fill = -1
    shape = -1
    amount = -1

    deck = []

    for c in range(3):
        color +=  b
        for f in range(3):
            fill += 1
            for s in range(3):
                shape += 1
                for a in range(3):
                    amount += 1

                    if color == 0:
                        Ccolor = 'red'
                    elif color == 1:
                        Ccolor = 'green'
                    elif color == 2:
                        Ccolor = 'purple'

                    if fill == 0:
                        Cfill = 'full'
                    elif fill == 1:
                        Cfill = 'half'
                    elif fill == 2:
                        Cfill = 'empty'

                    if shape == 0:
                        Cshape = 'rect'
                    elif shape == 1:
                        Cshape = 'bar'
                    elif shape == 2:
                        Cshape = 'wave'

                    if amount == 0:
                        Camount = 'one'
                    elif amount == 1:
                        Camount = 'two'
                    elif amount == 2:
                        Camount = 'three'
                    
                    card = [Ccolor, Cfill, Cshape, Camount]

                    deck.append(card)
                
                amount = -1
            shape = -1
        fill = -1
    color = -1

    return(deck)


if __name__ == "__main__":
    main()