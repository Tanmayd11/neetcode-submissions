class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            s1 = s
            s2 = t

            if sorted(s1) == sorted (s2):
                return (True)
            else :
                return (False)