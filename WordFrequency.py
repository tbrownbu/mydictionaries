infile = open('sometext.txt', 'r')
readfile = infile.read()

mydictionary = {}
wordlist = readfile.split(' ')


for words in wordlist:

    words = words.lower()
    words = words.replace('.','')
    words = words.replace(',','')
    words = words.replace('\n','')
    if words in mydictionary:
        mydictionary[words]=mydictionary[words]+1
    else:
        mydictionary[words]=1

print(mydictionary)
