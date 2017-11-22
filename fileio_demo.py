f = open("c:\\temp\\1.txt","r")
lst = []
for line in f:
    lst.append(line)
f.close()

f1 = open("c:\\temp\\2.txt","w")
for l in set(lst):
    f1.write(l)
f1.close()