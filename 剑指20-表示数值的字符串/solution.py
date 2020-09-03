# coding=utf-8

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            s_f = float(s)
        except ValueError as e:
            return False
        return True
