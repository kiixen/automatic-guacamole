import random
class FOD:
    def __init__(self):
        self.randomWords =["psycho","developer","melancholy"];
        self.currentWord = random.choice(self.randomWords)
        self.guessedLetters=[];
    def getHiddenSymbols(self):
        self.hiddenWord= ""
        for letter in self.currentWord:
            self.hiddenWord+=letter if letter in self.guessedLetters else "*" 
        return self.hiddenWord
    def guessLetterOrWord(self,letterOrWord):
        for letter in letterOrWord:
            if letter not in self.currentWord:
                raise Exception("Try agian.")
            self.guessedLetters.append(letter)
        return self.getHiddenSymbols()
    def loop(self):
        print("Game is started")
        while "*" in self.getHiddenSymbols():
            print(self.hiddenWord, len(self.hiddenWord))
            letterOrWord = input("Enter your Letter/Word:")
            try: 
                self.guessLetterOrWord(letterOrWord)
                print("ugadal")
            except Exception as e:
                    print(e)
        else:
            print("you won",self.hiddenWord)
game = FOD()
game.loop()