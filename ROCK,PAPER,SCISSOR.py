import random

options = ("rock", "scissor", "paper")

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Plz choose (rock, scissor, paper) ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("its Tie")
    elif player == "rock" and computer =="scissor":
        print("you Win")
    elif player == "scissor" and computer =="paper":
        print("you Win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    else:
        print("you lose")
    
    
    play_again = input("PLAY AGAIN: y or n = ").lower()
    if not play_again == "y":
        running = False
print("thanks for playing")
    
