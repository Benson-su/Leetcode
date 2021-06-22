class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        word_dict =  collections.defaultdict(list)
        for word in words:
            word_dict[word[0]].append(word[:])
        
        count = 0
        print(word_dict)
        for char in s:
            for rest in word_dict.pop(char, ()):
                if len(rest) > 1:
                    word_dict[rest[1]].append(rest[1:])
                else:
                    count += 1
        return count
                
            
