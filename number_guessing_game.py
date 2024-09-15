import random
def guess_num():
    num_guess=0
    number=random.randint(1,10)
    player_name=input("Hello! What's your name?\n")
    print("Okay,",player_name,". I'm guessing a number between 1 and 10:")

    while num_guess<5:
        guess=int(input())
        num_guess+=1
        if(guess<number):
            print("Your guess is too low!")
        elif(guess>number):
            print("Your guess is too high!")
        else:
            break
    if(guess==number):
        print("Congratulations! "+player_name+". You guessed the correct number in",num_guess,"tries!")
    else:
        print("Sorry! "+ player_name+", you did not guess the number. The number was",number,".")
guess_num()