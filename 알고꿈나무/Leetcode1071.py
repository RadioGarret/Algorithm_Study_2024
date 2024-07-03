class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        if str1+str2 == str2+str1:
            return str1[0:gcd(len(str1),len(str2))]
        return ""
