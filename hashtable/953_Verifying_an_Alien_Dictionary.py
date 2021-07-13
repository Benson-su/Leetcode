ass Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>len(words[i+1])-1:
                    return(False)
                elif order.index(words[i][j])<order.index(words[i+1][j]):
                    break
                elif order.index(words[i][j])==order.index(words[i+1][j]):
                    continue
                else:
                    return(False)
        return(True)
