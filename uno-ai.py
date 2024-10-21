# implemented plus two with Daniele Discenza, Jake Di Caprio, Panagiotis Stathopoulos:
import random 
def start_game():
    # THE SET UP OF UNO
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))
    

    deck = [(rank, colour) for rank in ranks for colour in colours]
    
    # plus_two deck
    plus_two_deck = [("Plus Two", colour) for colour in colours]

    # whole deck
    deck.extend(plus_two_deck)

    # shuffle the deck
    random.shuffle(deck)

    #dealing the hands
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]
    
    # central card
    central_card = deck.pop(0)
    # we  chose how this information is encoded
    # WE decide 0 = player 1, 1 = player 2
    main_loop(p1 , p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):
    
    #while p1 and p2:
    while len(p1) > 0 and len(p2) > 0:
        print(f"Player {whose_turn +1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_card}")

        ans = int(input("You have a choice. You can (0) draw or (1) play"))
        
        if ans == 1:
            #ask the user for a card to play
            # many ways we can get this information
            player_choice = int(input("Which card to play?")) - 1
            valid = valid_play(central_card, p1[player_choice])
            #IF their card is valid, 1. remove that card from the hand
            # 2. we need to place it on the face_up pile!!!
            if valid:
                central_card = p1.pop(player_choice)
                if central_card[0] == "Plus Two":
                    p2.append(deck.pop(0))
                    p2.append(deck.pop(0))

        if ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)
        # the end of the while loop, it will loop again
        # we will set up the data so the next loop works successfully
        p1, p2 = p2, p1 #replace player 1 hand w player 2
        whose_turn = (whose_turn + 1) % 2

def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

