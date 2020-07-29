from Python_intro import pig_latin_phrase

def reader(fname):
    with open(fname, "r") as f:
        for l in f:
            print(pig_latin_phrase(l.strip()))

reader('tswift.txt')
