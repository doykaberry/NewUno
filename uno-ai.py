# implemented plus two and reshuffling with Daniele Discenza, Jake Di Caprio, Panagiotis Stathopoulos:
import random 
def start_game():
    # THE SET UP OF UNO
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))
    plus_twos = ("+2",)
    

    deck = [(rank, colour) for rank in ranks for colour in colours]
    
    # plus_two deck
    plus_two_deck = [(plus_two, colour) for plus_two in plus_twos for colour in colours]

    # whole deck
    deck.extend(plus_two_deck)

    # shuffle the deck
    random.shuffle(deck)

    #dealing the hands
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]
    
    # central card
    central_card = deck.pop(0)

    # face up pile
    face_up_pile = [central_card]

    # we  chose how this information is encoded
    # WE decide 0 = player 1, 1 = player 2
    main_loop(p1 , p2, deck, central_card, 0, face_up_pile)

def main_loop(p1, p2, deck, central_card, whose_turn, face_up_pile):

    #while p1 and p2:
    while len(p1) > 0 and len(p2) > 0:
        if whose_turn == 0:
                
            print(f"Player {whose_turn +1}'s turn, here is your hand: {p1} \n")
            print(f"Central card is: {central_card}\n")

            ans = int(input("You have a choice. You can (0) draw or (1) play: \n"))

            if len(deck) == 0:
                print("Shuffling deck\n\n")
                deck.extend(face_up_pile)
                random.shuffle(deck)
                deck.remove(central_card)
                face_up_pile.clear()
                face_up_pile.append(central_card)
            
            if ans == 1:
                #ask the user for a card to play
                # many ways we can get this information
                player_choice = int(input("Which card to play?: \n")) - 1
                print("\n")
                valid = valid_play(central_card, p1[player_choice])
                #IF their card is valid, 1. remove that card from the hand
                # 2. we need to place it on the face_up pile!!!
                if valid:
                    central_card = p1.pop(player_choice)
                    print(f"The central card is: {central_card}\n")
                    print("\n")
                    face_up_pile.insert(0, central_card)
                    if central_card[0] == "+2":
                        p2.append(deck.pop(0))
                        if len(deck) == 0:
                            print("Shuffling deck\n\n")
                            deck.extend(face_up_pile)
                            random.shuffle(deck)
                            deck.remove(central_card)
                            face_up_pile.clear()
                            face_up_pile.append(central_card)

                        p2.append(deck.pop(0))

            if ans == 0:
                print("\n")
                draw_card = deck.pop(0)
                p1.append(draw_card)
        else: #this means its p2 turns aka the AI
            central_card = ai_turn(p2, central_card, deck, face_up_pile, p1)

        # the end of the while loop, it will loop again
        # we will set up the data so the next loop works successfully

        whose_turn = (whose_turn + 1) % 2

    if len(p1) == 0:
        print("p1 is the winner!")
    if len(p2) == 0:
        print("p2 is the winner!")

def ai_turn(ai_hand, central, deck, face_up_pile, p1):
    ai_played = False
    for card in range(len(ai_hand)):
        if valid_play(ai_hand[card], central):

            if central[0] == "+2":
                p1.append(deck.pop(0))
                if len(deck) == 0:
                    print("Shuffling deck]\n\n")
                    deck.extend(face_up_pile)
                    random.shuffle(deck)
                    deck.remove(central)
                    face_up_pile.clear()
                    face_up_pile.append(central)

                p1.append(deck.pop(0))

            print(f"p2 placed a: {ai_hand[card]}\n")
            print("\n")
            central = ai_hand.pop(card)
            face_up_pile.insert(0, central)
            ai_played = True
            break
    if not ai_played:
        if len(deck) == 0:
            print("Shuffling deck\n\n")
            deck.extend(face_up_pile)
            deck.remove(central)
            random.shuffle(deck)
            face_up_pile.clear()
            face_up_pile.append(central)
        print("p2 drew a card\n")
        print("\n")
        ai_hand.append(deck.pop(0))

    return central


def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1
                                                     ]
start_game()
