class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
    
        for i in range(1,n):# end of first number
            if num[0] == '0' and i > 1:
                break
            a = int(num[:i])

            for j in range(i+1,n):# end of second number
                if num[i] == '0' and j - i > 1:
                    break
                b = int(num[i:j])

                k = j  
                count = 2
                aa, bb = a, b

                while k < n:
                    cc = aa + bb
                    s = str(cc)
                
                    if not num.startswith(s, k):
                        break
                
                    k += len(s)
                    aa, bb = bb, cc
                    count += 1

                if k == n and count >= 3:
                    return True
        return False
