class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPredecessor(s1,s2):
            add = False
            s1_inx = 0
            s2_inx = 0
            while s1_inx < len(s1) and s2_inx < len(s2):
                if s1[s1_inx] == s2[s2_inx]:
                    s1_inx += 1
                    s2_inx += 1
                elif add == False:
                    s2_inx += 1
                    add = True
                else:
                    return False
            return True
        words.sort(cmp=lambda x,y:len(x) - len(y))
        dp = [1] * len(words)
        res = 1
        for i in range(len(words)):
            for j in range(0,i):
                if len(words[i]) == len(words[j]):
                    break
                elif len(words[i]) - 1 > len(words[j]):
                    continue
                else:
                    if isPredecessor(words[j],words[i]):
                        dp[i] = max(dp[i],dp[j]+1)
                        res = max(res,dp[i])

        return res       
