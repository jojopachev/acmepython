import json
import itertools

def load_words():
    i = 0
    with open("words_dictionary.json", "r") as f:
        data = json.load(f)
    return data
    #for word in data:
        #if word[0] == "a":
            #i+=1
        
    #print(f"There are {i} words that start with 'A'")
    
def sort(string):
    return ''.join(sorted(string))
    
def perm(word):
    a = []
    for perm in itertools.permutations(word):
        a.append("".join(perm))
    return a

def anagram_finder(word, Richard):
    Anne = []
    for w in perm(word):
        if w in Richard:
            Anne.append(w)
    return Anne

def anagram_finder2(word, dic):
    a = []
    for w in dic:
        if sort(word) == sort(w):
            a.append(''.join(w))

    return a

if __name__ == "__main__":
    i = input("Enter a word or list of letters:")
    d = load_words()
    if len(i) > 8:
        a = anagram_finder2(i, d)
    else:
        a = anagram_finder(i, d)
    print(f"The anagrams of {i} are:{' '.join(a)}")
    #perm("cat")
    #print(sort("zxcvbnmlkjhgfdsaqwertyuiop"))
