function uc_first(s){
	l = s.slice(1)
	return s[0].toUpperCase() + l.toLowerCase();  
}

function pig_latin(word) {
    var vowel = "aeiou";
    var punc = ",.!?:;-";
    var p = "";
	if(!word){
		return '';    
	}
	if(punc.includes(word[word.length-1])){
        return pig_latin(word.slice(0,word.length-1)) + word[word.length-1];
	}
    if(vowel.includes(word[0])) {
        p = word + "hay";
    }
    else {
        p = word.slice(1) + word[0] + "ay";   
    }
	var c = word[0].toUpperCase()
	if(word[0] == c){
		return uc_first(p);
	}
	console.log(uc_first("HEllo")) 
    return p;

}

function pig_latin_phrase(phrase){
	phrase = phrase.split(" ");
	var translation = []
	for (var i = 0; i <= phrase.length; i++){
		translation.push(pig_latin(phrase[i]));			
	}
	return translation.join(" ");
}

function handle_input()
{
    var d = document.getElementById("input").value;
    document.getElementById("output").innerHTML = pig_latin_phrase(d);
    
}

console.log(pig_latin_phrase("hello"))
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
 
