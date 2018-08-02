#to lower case:
class Solution:
    def toLowerCase(self, string):
        res = ''
        for i, c in enumerate(string):
            if(c >= 'A' and c <= 'Z'):
                res += chr(ord(c) - ord('A') + ord('a'))
            else:
                res += c
        return res

#morse_code:
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        dict_map = {
         "a":".-","b":"-...","c":"-.-.","d": "-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-",
         "y":"-.--",
         "z":"--.."}
        morse_word_list = []
        for word in words:
            morse_word = ""
            for char in word:
                morse_char = dict_map[char]
                morse_word += morse_char
            if morse_word not in morse_word_list:
                morse_word_list.append(morse_word)
        return len(morse_word_list)

#judge route circle:
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

#class reverse a string:
class Reverse(object):
    def reverse_string(s):
        lst = list(s)
        for i in range(len(lst)/2):
            lst[i], lst[len(lst) -i -1 ] =lst[len(lst) -i -1 ], lst[i]
        return ''.join(lst)
#reverse letters in each word in a list
    def reverse_within_list(in_lst):
        new_lst =[]
        for word in in_lst:
            new_lst.append(reverse_string(word))
        return new_lst

#Goat Latin:

class Solution(object):
    def toGoatLatin(self, S):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        return ' '.join([
            (token + 'ma' if token[0] in vowels else token[1:] + token[0] + 'ma') + 'a'*(i+1)
            for i, token in enumerate(S.split(' '))
        ])

#Check Capital letters:

class Solution(object):
    def detectCapitalUse(self, word):
        if word == word.upper():
            return True
        if word == word.lower():
            return True

        check = word[0].upper() + word[1:].lower()
        if (word == check):
            return True
        else:
            return False

#Rotate digits:
class Solution3(object):
    def rotatedDigits(self, N):
        invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        result = 0
        for i in xrange(N+1):
            lookup = set(list(str(i)))
            if invalid & lookup:
                continue
            if diff & lookup:
                result += 1
        return result

#count binary strings:
class Solution(object):
    def countBinarySubstrings(self, s):
        result, prev, curr = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        result += min(prev, curr)
        return result

#most common word:

def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        # maintain dict of word frequency of words which are not in banned
        hashmap = {}
        mostcommon = ''
        count = 0
        for word in paragraph.split():
            word = word.strip('!?\',;.').lower()
            # while inserting words in frequency keep track of most frequent word
            if word not in banned:
                hashmap[word] = hashmap.get(word,0) + 1
                if hashmap[word] > count:
                    count = hashmap[word]
                    mostcommon = word
        return mostcommon

#ransomnote from magazine:

def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    s1 = set(ransomNote)
    s2 = set(magazine)

    for i in s1:
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

#first unique letter from word

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = dict([])
        for c in s:
            if cnt.has_key(c):
                cnt[c] += 1
            else:
                cnt[c] = 1
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
