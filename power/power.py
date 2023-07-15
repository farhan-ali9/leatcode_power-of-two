# first solution
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0: 
            return False
        else:
            return bin(n).count('1') == 1


#second solution 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n%2==0:
                n//=2
            elif n==1:
                    return True
            else:
                return false
