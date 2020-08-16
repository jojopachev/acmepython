from itertools import product

def sphere_volume(r):
    ''' finds the volume of a sphere'''
    v = ((4./3)*(3.14159)*r**3)
    return v

def isolate(a,b,c,d,e):
    '''isolates the first 2 variables with 5 spaces and the last 3 with 1'''
    print(a,b,c, sep="     ",end=' ')
    print(d,e)

def first_half(a):
    '''returns the first half of str a'''
    l = (len(str(a))/2 + 0.5)   
    l = int(l)
    return a[:l]

def backward(b):
    ''' reverses a string'''
    return str(b)[::-1]

def list_ops():
    my_list = ["bear", "ant", "cat", "dog"]
    my_list.append("eagle")
    my_list[2] = "fox"
    my_list.pop(1)
    my_list[1] = "hawk"
    my_list.sort(reverse = True)
    my_list[-1] = "bear hunter"
    print(my_list)

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
    return " ".join(translation)

def palindrome():
    bp = 0
    for i, j in product(range(100, 1000), range(100, 1000)):
        s = str(i*j)
        if s == s[::-1]:
            if j*i > bp:
                bp = j*i
    print(bp)
    
def alt_harmonic(n):
    a = [((-1)**(i+1))/i for i in range(1, n+1)]
    return sum(a)

if __name__ == "__main__":
    #i = input()
    #print("Hello, world!\n"*100)
    s =  sphere_volume(3)   
    #print(s)
    #isolate(1,2,3,4,5)
    h = first_half("hello")
    #print(h)
    b = backward("hello")
    #print(b)
    #list_ops()
    p = pig_latin_phrase("hello")
    #print(p)
    #palindrome()
    a = alt_harmonic(10**5)
    print(a)
