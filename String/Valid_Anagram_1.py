class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in range(0,len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] +=1


        for j in range(0,len(t)):
            if t[j] in d:
                d[t[j]]-=1
            else:
                continue

        l = list(d.values())
        s = list(set(l))
        if s[0] == 0:
            return True
        else:
            return False
