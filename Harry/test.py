'''import random

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
print(game_bot)'''
def table():
    st =[]

    for j in range(1,21):
        val =str(f"{2} x {j} = {2*j}")
        st.append(val)
    return st

print(table())