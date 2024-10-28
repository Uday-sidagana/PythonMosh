import random

def bot():
    Game_bot =""

    val = int(10*(random.uniform(1, 1.3)))
    if val == 10:
        Game_bot = "Rock"
    elif val == 11:
        Game_bot = "Paper"
    elif val == 12:
        Game_bot = "Scissor"
    return Game_bot

game_bot = bot()

def game(game_bot):
    Choose = input('"Rock", "Paper", "Scissor"')
    

    if Choose== game_bot:
        print(f"You choose: {Choose} and bot choose: {game_bot}, DRAW!!")
    elif Choose == "Rock" and game_bot == "Paper":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Lose")

    elif Choose == "Rock" and game_bot == "Scissor":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Win")

    elif Choose == "Paper" and game_bot == "Scissor":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Lose")

    elif Choose == "Paper" and game_bot == "Rock":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Win")  

    elif Choose == "Scissor" and game_bot == "Rock":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Lose")

    elif Choose == "Scissor" and game_bot == "Paper":
        print(f"You choose: {Choose} and bot choose: {game_bot}, You Win")

game(game_bot)