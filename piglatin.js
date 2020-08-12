function uc_first(s){
	l = s.slice(1)
	return s[0].toUpperCase() + l.toLowerCase();  
}

var vowel = "aeiou";
var punc = ",.!?:;-";

function pig_latin(word) {
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
    else if(word[0]=="h") p = word.slice(1) + "-" + word[0] + "ay"
    else {
        p = word.slice(1) + word[0] + "ay";   
    }
	var c = word[0].toUpperCase()
	if(word[0] == c){
		return uc_first(p);
	}
    return p;

}
function validPigLatin(word){
    if(word.length < 3) return false;
    if(word.slice(word.length-2) != "ay") return false;
    if(vowel.includes(word[word.length-3])) return false;
    return true;
}

function inverse_piglatin(word){
    var n = "";
    if(!word) return word;
    if(punc.includes(word[word.length-1])){
        return inverse_piglatin(word.slice(0,word.length-1)) + word[word.length-1];
	}
    if(!validPigLatin(word)) return word;
	if(word[word.length-3] == "h"){
        if(word[word.length-4] == "-"){
            n = word[word.length-3] + word.slice(0,word.length-4);
        }
        else {
           n = word.slice(0,word.length-3);
        }
    }
    else{
        n = word[word.length-3] +  word.slice(0,word.length-3);
    }
    var c = word[0].toUpperCase()
	if(word[0] == c){
		return uc_first(n);
	}
    return n;
}

function pig_latin_phrase(phrase){
	phrase = phrase.split(" ");
	var translation = []
	for (var i = 0; i <= phrase.length; i++){
		translation.push(pig_latin(phrase[i]));			
	}
	return translation.join(" ");
}

function inverse_pig_latin_phrase(phrase){
	phrase = phrase.split(" ");
	var translation = []
	for (var i = 0; i <= phrase.length; i++){
		translation.push(inverse_piglatin(phrase[i]));
	}
	return translation.join(" ");
}

console.log(inverse_pig_latin_phrase("Ello-hay orldway, ello-hay orldway"));

function handle_input()
{
    var d = document.getElementById("input").value;
    document.getElementById("output").innerHTML = pig_latin_phrase(d);
    
}

new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        english: "",
        pig: "",
	direction: true,
    },

    methods: {
        updateEnglish(val) {
            if (!val) this.english = null;
            this.english = inverse_pig_latin_phrase(val);
        },
        updatePig(val) {
            if (!val) this.english = null;
            this.pig = pig_latin_phrase(val);
        },
        changeFocus() {
            if(this.direction == true) {
	            this.$refs.tEnglish.focus();
	        }
	        else{
	            this.$refs.tPig.focus();    
	        }
	    }
    },
/*    computed: {
        translation() {
            if (!this.input) return null;
            return pig_latin_phrase(this.input);
        }
    }*/
});
