string1 = "abcdefg"
string2 = "abcdefa"
string3 = "abc123"
string4 = "abc1231"
string5 = "!@#$%^&*()_+<>? "
string6 = " !@#$%^&*()_+<>? "

# method 1.1.1
def solution(s):
    letterDictionary = {}
    for letter in s:
        if letter not in letterDictionary:
            letterDictionary[letter] = 1
        else:
            letterDictionary[letter] += 1
    if sum(letterDictionary.values()) == len(letterDictionary):
        return True
    else:
        return False
    
# test
print solution(string1)
print "Expected: True"

print solution(string2)
print "Expected: False"

print solution(string3)
print "Expected: True"

print solution(string4)
print "Expected: False"

print solution(string5)
print "Expected: True"

print solution(string6)
print "Expected: False"
