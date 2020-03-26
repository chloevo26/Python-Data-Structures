def anagram(s,t):
    s = s.replace(' ', '')
    t = t.replace(' ', '')
    letterArr = []
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        letterArr.append(s[i].lower())

    for j in range(len(t)):
        for i in range(len(letterArr)):
            if t[j] == letterArr[i]:
                letterArr.pop(i)
                break
        else:
            return False
    return True



# ------------------ TEST --------------------
print(anagram('go go go','gggooo'))
print(anagram('abc', 'cba'))
print(anagram('hi man', 'hi    man'))
print(anagram('aabbcc', 'aabbc'))
print(anagram('123', '1 2'))

