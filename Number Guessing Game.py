# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:37:14 2022

@author: ronni
"""

import random
attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score. It's yours for the taking")
    else:
        print("The current highscore is {}".format(min(attempts_list)))
        
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello bigman! Welcome to the game of guesses!")
    player_name = input("Enter your name: ")
    wanna_play = input("Hi, {}, would you like the guessing game? (Enter Yes/No): ".format(player_name))
    
    #Attempts board
    attempts = 0
    show_score()
    
    while wanna_play.lower() == "yes":
        try:
            guess_number = input("Pick a number between 1 and 10: ")
            
            if int(guess_number) < 1 or int(guess_number) > 10:
                raise Exception("Please choose a number from the given range")
                
            if int(guess_number) == random_number:
                print("Wow! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took  you {} attempts.".format(attempts))
                
                play_again = input("Would you like to play again? (Enter Yes/No): ")
                
                if play_again.lower() == "yes":
                    attempts = 0
                    show_score()
                else:
                    print("Wazi king!")
                    break
            
            elif int(guess_number) < random_number:
                print("It's higher than this")
                attempts += 1
                
            elif int(guess_number) > random_number:
                print("It's lower")
                attempts += 1
                
        except:
            print("That is not a valid value. Try again!")
    else:
        print("That's cool. ")
        

if __name__ == "__main__":
    start_game()