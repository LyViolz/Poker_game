from bakery import assert_equal
def convert_card(value: int)-> str:
    """Converts a card valut to string
        value :int to str
        
    """
    if value==10:
        return 'X'
    elif value == 11:
        return 'J'
    elif value== 12:
        return 'Q'
    elif value == 13:
        return 'K'
    elif value == 14:
        return 'A'
    else:
        return str(value)

def hand_to_string(hand: list[int])-> str:
    """converts a list to string 
        parameters hand: list[str]
        
    """
    return convert_card(hand[0])+" "+convert_card(hand[1])+" " +convert_card(hand[2])

def sort_hand(hand: list[int])-> list[int]:
    """Sorts a list of three integers from largest to smallest
        parameters: hand list[int]
        
    """
    if hand[0]<hand[1]:
        hand[0], hand[1] = hand[1], hand[0]
    if hand[0]< hand[2]:
        hand[0], hand[2] = hand[2], hand[0]
    if hand[1]< hand[2]:
        hand[1],hand[2]= hand[2], hand[1]
    return hand
def has_triple(hand: list[int])-> bool:
    """ True if there are 3 identical cards if not false
        parameters hand list[int]
        
    """
    return hand[0]==hand[1] == hand[2]

def has_straight(hand: list[int])-> bool:
    """if consecutive and from largest to smallest then result is true
        parameters: hand list[int]
    """
    
    
    return hand[0] == hand[1]+ 1 and hand[1] == hand[2] + 1

def has_pair(hand: list[int])-> bool:
    """  Return True if the list has two identical numbers (a "pair");
        parameter : hand list [int]
    """
    return hand[0]==hand[1] or hand[1]==hand[2]

def score_hand(hand: list[int])->int:
    """
    Returns the scores depends on the previous functions
    score calculated with base-16
    parameters: hand list[int]
    """
    if has_triple(hand):
        score=16
    elif has_straight(hand):
        score= 15
    elif has_pair(hand):
        score= hand[1]
    else:
        score = 0
        
    new_score = (score* 16**3)+ (hand[0]* 16**2)+(hand[1]* 16**1)+(hand[2])
    return new_score

def dealer_plays(hand: list[int])-> bool:
    """
    The highest card is Queen, which is true and check feature card
    parameter: hand list[int]
    
    """
    new_score=score_hand(hand)
    score= new_score//(16**3)
    return score> 0 or hand [0] >=12


def play_round() -> int:
    
    player_hand = deal()
    dealer_hand = deal()

    player_hand_sorted = sort_hand(player_hand)
    dealer_hand_sorted = sort_hand(dealer_hand)
    
    print("Your hand:", hand_to_string(player_hand_sorted))
    print("Dealers hand:", hand_to_string(dealer_hand_sorted))

    choice = get_choice()

    if choice == 'f':
        print("fold.")
        return -10

    
    dealer_play = dealer_plays(dealer_hand_sorted)
    
 
    if dealer_play:
        player_score = score_hand(player_hand_sorted)
        dealer_score = score_hand(dealer_hand_sorted)
        
        if player_score > dealer_score:
            print("You win")
            return 20 
        elif player_score < dealer_score:
            print("You lose")
            return -20  
        else:
            print("tie")
            return 0 

    else:
        print("Dealer folds.")
        return 10 


def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")