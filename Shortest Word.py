#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.



def find_short(s):
    i=s.split()
    l=min([(word,len(word))for word in i],key=lambda x:x[1])
    l=l[1]
    return l # l: shortest word length
