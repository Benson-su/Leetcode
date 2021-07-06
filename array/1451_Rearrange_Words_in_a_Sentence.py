class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        len_dict = {}
        ret = ""
        text = text[0].lower() + text[1:]
        for letter in text.split(" "):
            if len(letter) not in len_dict:
                len_dict[len(letter)] = [letter]
            else:
                len_dict[len(letter)].append(letter)
        for length in sorted(len_dict.keys()):
            for letter in len_dict[length]:
                ret += (letter+" ")
        ret = ret[:-1]
        ret = ret[0].upper() + ret[1:]
        return ret
        
