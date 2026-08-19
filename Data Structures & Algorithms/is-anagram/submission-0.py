class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = sorted(s)
        t_ = sorted(t)

        if len(s_) != len(t_):
            return False
        
        for i in range(len(s_)):
            if s_[i] != t_[i]:
                return False
        return True