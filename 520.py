class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n <= 1:
            return True
        if word[0].isupper() and word[1].isupper():
            for ch in word[2:]:
                if not ch.isupper():
                    return False
        else:
            for ch in word[1:]:
                if not ch.islower():
                    return False
        return True 
        


        