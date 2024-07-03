import random  

def get_user_choice():
    choice = input("Enter a choice (rock/paper/scissors): ")
    return choice

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def winner(user, computer):
    if user == computer:
        return "Tie!"
    elif(user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "You win!"
    else: 
        return "Computer wins!"

def main():
    my_choice= get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {my_choice}") 
    print(f"computer chose {computer_choice}")
    result= winner(my_choice, computer_choice)
    print(result)

if __name__=="__main__":
    main()
    


