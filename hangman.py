import random
import json

def load_words():
    i = 0
    with open("words_dictionary.json", "r") as f:
        data = json.load(f)
    return data


class Hangman():
    
    def __init__(self, word):
        self.guesses = set()
        self.dic = load_words()
        self.w = self.rand_word()
        self.partial_word = [' '] * len(self.w)
    
    def rand_word(self):
        lis = list(self.dic)
        r = random.randint(0, len(lis))
        return lis[r]
    
    def is_valid_guess(self,c):
        if type(c) is not str:
            return False
        else: return True
    
    def guess(self, c):
        if self.is_valid_guess(c):
            if c in self.w:
                self.guesses.add(c)

    def update_partial(self, c):
        for i, letter in enumerate(self.w):
            if c == letter:
                self.partial_word[i] = c
    
    
if __name__ == "__main__":
    d = load_words()
    h = Hangman("hello")
    h.guess("r")
    print(h.partial_word)
    h.guess("e")
    print(h.partial_word)
