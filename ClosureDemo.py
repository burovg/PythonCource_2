def Count():
    counter = [0]
    def DoCount():
        counter[0] += 1
        return counter[0]
    return DoCount

num = Count()
print num()
print num()
print num()
