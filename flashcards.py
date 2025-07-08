class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word +" ("+self.meaning+") "
    
flash = []
print("Welcome to the flashcard application.")

# loop is added here so that user can keep adding flashcards
# stops when user deems
while(True):
    word = input("Enter your term here:")
    meaning = input("Enter the definition here:")

    flash.append(flashcards(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard, or 1 if you want to stop:"))

    if option:
        break

# printing the flashcards
print("Your flashcards:")
for i in flash:
    print(">", i)