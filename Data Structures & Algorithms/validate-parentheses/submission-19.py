class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        pile = []
        
        for x in s:
            if x in pairs:
                last = pile.pop() if pile else None

                if last != pairs[x]:
                    return False
            else:
                pile.append(x)
        return len(pile) == 0