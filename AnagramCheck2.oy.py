def anagram(s,t):
    s = s.replace(' ','')
    t = t.replace(' ', '')
    if len(s) != len(t):
        return False
    else:
        dict = {}
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        for letter in t:
            if letter not in dict or dict[letter] == 0:
                return False
            else:
                dict[letter] -= 1
    return True


print(anagram('hello world', 'he llo world'))
print(anagram('go go go','gggooo'))
print(anagram('abc', 'cba'))
print(anagram('hi man', 'hi    man'))
print(anagram('aabbcc', 'aabbc'))
print(anagram('123', '1 2'))