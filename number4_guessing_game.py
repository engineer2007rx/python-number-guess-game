import random
import art

def random_number():
    return random.choice(range(1,101))

def deficulty_level():
    a = input("type e for easy level, h for hard level ")
    if a=="e":
        return int(10)
    else:
        return int(5)

def user_guess():
    return int(input("what is your guess "))

 

def play_game():
    print(art.logo)
    print("welcome to number guessing game")
    lives= deficulty_level()
    rnumber= random_number()
    print(f"okk you have {lives} lives")
    is_game_end = False
    while not is_game_end:
        kk= user_guess()
        if kk>rnumber:
           print("too big")
           lives -=1
           print(f"you have {lives} remaining")
           if lives<=0:
              print(f"you lose, number was {rnumber}")
              is_game_end= True
        elif kk< rnumber:
           print("too small")
           lives -=1
           print(f"you have {lives} remaining")
           if lives<=0:
              print(f"you lose, number was {rnumber}")
              is_game_end= True
        else:
            print("congratulation, you win the game  ")
            is_game_end= True


while input("you want to play number guessing game , yes or no ") =="yes":
      
      play_game()           






    
