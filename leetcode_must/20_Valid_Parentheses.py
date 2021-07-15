class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = [] #'()'
        for item in s:
            if len(par) > 0:
                if item == "(":
                    par.append("(")
                elif item == "{":
                    par.append("{")
                elif item == "[":
                    par.append("[")
                elif item == ")":
                    if par[-1] != "(":
                        return False
                    else:
                        par.pop()
                elif item == "}":
                    if par[-1] != "{":
                        return False
                    else:
                        par.pop()
                elif item == "]":
                    if par[-1] != "[":
                        return False
                    else:
                        par.pop()
            else:
                par.append(item)
        if len(par) > 0:
            return False
        return True
            
