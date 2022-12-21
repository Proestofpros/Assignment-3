for i in range(1000):
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
            print( word_count(wor))

    for w in worde:
        dicti[w]=dicti.get(w,0)+1
    for k,v in dicti.items():
        print(k,'occured',v,'times')
    for a in range (100):
        print(word_count(word))