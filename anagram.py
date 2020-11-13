import json

def load_words():
    i = 0
    with open("words_dictionary.json", "r") as f:
        data = json.load(f)
    for word in data:
        if word[0] == "a":
            i+=1
        
    print(f"There are {i} words that start with 'A'")
    
if __name__ == "__main__":
    load_words()
