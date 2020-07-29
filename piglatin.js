function pig_latin(word) {
    var vowel = "aeiou";
    var punc = ",.!?:;-";
    var p = "";
    
    if(vowel.includes(word[0])) {
        p = word + "hay";
    }
    else {
        p = word.slice(1) + word[0] + "ay";   
    }
    return p;
}

function handle_input()
{
    var d = document.getElementById("input").value;
    console.log(pig_latin(d));
}

console.log(pig_latin("ello"))
/*
def uc_first(s):
    return s[0].upper() + s[1:].lower()

def pig_latin(word):
    vowel = "aeiou"
    punc = ",.!?;:-"
    if len(word) == 0:
        return word
    if word[-1] in punc:
        return pig_latin(word[:-1]) + word[-1]
    if word[0] in vowel:
        p = word + "hay"
    else:
        p = word[1:] + word[0] + "ay"
    if word[0].isupper():
        p = uc_first(p)
    return p
    
def pig_latin_phrase(phrase):
    phrase = phrase.split(" ")
    translation = []  
    for w in phrase:
        translation.append(pig_latin(w))
    return " ".join(translation)*/
 
