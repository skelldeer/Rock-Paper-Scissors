import random 

human_score=0
ai_score=0

rounds = int(input("choose number of rounds :"))

choice = { 'rock':1, 'paper':2, 'scissors':3}


while (human_score < rounds and ai_score < rounds) :

    ai_choice = choice[random.choice(list(choice.keys()))]

    human_choice = choice[input("your choice: ")]

    if human_choice - ai_choice in [1, -2]:
        print("your won the round !")
        human_score += 1
        print(f"You: {human_score}|Computer: {ai_score}")
        print()
    elif human_choice - ai_choice in [-1, 2]:
        print("computer won the round !")
        ai_score +=1
        print(f"You: {human_score}|Computer: {ai_score}")
        print()
    else:
        print("Tie !")
        print(f"You: {human_score}|Computer: {ai_score}")
        print()

if human_score == rounds :
    print("you won the game !")
else :
    print("computer won the  game !")

    
    
    
    
    