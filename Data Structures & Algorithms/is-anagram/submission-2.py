class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s = s.lower()
        t = t.lower()

        s = list(s)
        t = list(t)

        for letter in s:
            if not letter in t:
                return False
            else:
                t.remove(letter)

        return True
        