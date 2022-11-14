import random

class GuessTheNumberGame:
    def __init__(self):
        self.options = [1,2,3,4,5,6,7,8,9,10]
        self.correct_answer = random.randint(1,10)
        self.guessed_list = list()
    
    def compare_answer(self, guessed):
        try :
            guessed_answer = int(guessed)
            if guessed_answer == self.correct_answer:
                print(f"You win the game! The correct answer was {guessed_answer}")
                self.winnings()
                return 1
            elif guessed_answer in self.guessed_list:
                print(f"You have already guessed {guessed_answer}. Try again!")
                self.guessed_list.append(guessed_answer)
                return 0
            elif guessed_answer not in self.options:
                print(f"{guessed_answer} is not in range 1-10. Try again!")
                self.guessed_list.append(guessed_answer)
                return 0
            else:
                print(f"Nice try, but {guessed_answer} is not correct. Try again!")
                self.guessed_list.append(guessed_answer)
                return 0
        except:
            print("That answer is not option. Try an integer.")
            return 0


    def winnings(self):
        wrong_guesses = len(self.guessed_list)
        print(f"You made {str(wrong_guesses)} incorrect guesses.")
    def play_game(self):
        winner = 0
        while winner < 1:
            print("Make your guess!")
            guessed_answer = input()
            winner = self.compare_answer(guessed_answer)
