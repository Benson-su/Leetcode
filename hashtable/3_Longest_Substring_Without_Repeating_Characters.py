class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_hash = ''
        right = 0
        max_len = 0
        while right < len(s):
            while s[right] in char_hash:
                char_hash = char_hash[1:]

            if s[right] not in char_hash:
                char_hash += (s[right])
                right += 1
                max_len = max(max_len, len(char_hash))

        return max_len
