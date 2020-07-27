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

def pig_latin(word):
    vowel = "aeiou"
    if word[0] in vowel:
        return word + "hay" 
    else:
        p = word[1:] + word[0] + "ay"
        return p
    
def pig_latin_phrase(phrase):
    phrase = phrase.split(" ")
    translation = []  
    for w in phrase:
        translation.append(pig_latin(w))
    return " ".join(translation)

if __name__ == "__main__":
    i = input()
    #print("Hello, world!\n"*100)
    s =  sphere_volume(3)   
    #print(s)
    #isolate(1,2,3,4,5)
    h = first_half("hello")
    #print(h)
    b = backward("hello")
    #print(b)
    #list_ops()
    p = pig_latin_phrase(i)
    print(p)
