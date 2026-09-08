class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_t = {}
        count_s = {}
        for letter in s:
            if letter not in count_s:
                count_s[letter] = 1
            else:
                count_s[letter] += 1
        
        for letter in t:
            if letter not in count_t:
                count_t[letter] = 1
            else:
                count_t[letter] += 1
        if count_t == count_s:
            return True
        return False