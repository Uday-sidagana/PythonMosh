import random


score =[]
for i in range(1,3):
    guess_number = int(100*random.uniform(0,1))
    # print(guess_number)
    
    
    def GuessingGame():
        count = 1
        my_guess = int(input(f"Enter Your Guess  Player{i}"))
        while my_guess != guess_number:

            if my_guess > guess_number:
                print("Your Guess is Bigger than the number, try something Lower!")
                count += 1
                my_guess = int(input("Enter Your Guess "))

            elif my_guess < guess_number:
                print("Your Guess is Smaller than the number, try something Higher!")
                count +=1
                my_guess = int(input("Enter Your Guess "))

        else:
            print("You Guessed it right!!")
            print(f"You took {count} no. of chances.")
            score.append(count)
    GuessingGame()
    

if score[0] < score[1]:
    print("Player 1 Won")

elif score[0] > score[1]:
    print("Player 2 Won")

else:
    print("Draw")






