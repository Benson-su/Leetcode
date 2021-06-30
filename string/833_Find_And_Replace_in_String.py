class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        ans = ""
        i = 0
        while i < len(s):
            if i not in indices:
                ans += s[i]
                i += 1
            else:
                ind = indices.index(i)
                source = sources[ind]
                target = targets[ind]
                part = s[i : i + len(source)]
                if part == source:
                    ans += target
                else:
                    ans += part
                i += len(source)
        return ans

