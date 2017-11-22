def compare(str1,str2) :
    str = [str1,str2]
    v1 = map(lambda x: len(x),str)
    m = max(v1)
    print str[v1.index(m)]

compare("asdfgaaaaaaaaaaaaaaaaaaa","123456789")

def concat(str1,str2):
    return str1 + str2

def printconcat(obj,str1,str2) :
    print obj(str1,str2)

printconcat(concat,"111","222")








