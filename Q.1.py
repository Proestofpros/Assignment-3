word=input('enter a word : ')
worde=word.replace(" ","")
dicti={}
def word_count(str):
    counts = dict()
    words = str.split()
    for wor in words:
        if wor in counts:
            counts[wor] += 1
        else:
            counts[wor] = 1
    return counts
def count(str):
    a=word_count(word)
    for w in a:
        a[w]=a.get(w,0)
    for k,v in a.items():
        print(k,'occured',v,'times')
def Letter_count(str):
    for w in worde:
        dicti[w]=dicti.get(w,0)+1
    for k,v in dicti.items():
        print(k,'occured',v,'times')
Letter_count(worde)
count(word)
