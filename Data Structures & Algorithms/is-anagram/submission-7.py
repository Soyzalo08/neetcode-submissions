class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cuenta_s = {}
        cuenta_t = {}
        if len(s) != len(t):
            return False

        for letra in s:
            if letra in cuenta_s:
                cuenta_s[letra] += 1
            else:
                cuenta_s[letra] = 1
        
        for letra in t:
            if letra in cuenta_t:
                cuenta_t[letra] += 1
            else:
                cuenta_t[letra] = 1

        if cuenta_s == cuenta_t:
            return True
        else:
            return False