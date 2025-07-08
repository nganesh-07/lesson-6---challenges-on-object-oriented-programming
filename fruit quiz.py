import random
class fruitquiz:

    # create a constructor
    def __init__(self):
        # create a dictionary of fruit as keys and their colors r stored as values
        self.fruits = {"strawberry": "red",
                       "banana": "yellow",
                       "grapes": "purple",
                       "watermelon": "green"}
    
    # choosing a random fruit for quiz
    def quiz(self):
        while(True):
            
            fruit, color = random.choice(list(self.fruits.items()))
            
            print("What is the color of", fruit)
            user_answer = input()

            if user_answer.lower() == color:
                print("Correct!")
            else:
                print("Try again.")
            
            option = int(input("Enter a 0 if you wanna play again, enter 1 if you wish to exit:"))
            
            if option:
                break

print("welcome to the fruit games")
fq = fruitquiz()
fq.quiz()