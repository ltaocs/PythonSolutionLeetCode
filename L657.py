class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        CharList = list(moves)
        R_Count = CharList.count('R')
        L_Count = CharList.count('L')
        U_Count = CharList.count('U')
        D_Count = CharList.count('D')
        if (R_Count == L_Count and U_Count == D_Count):
            return True
        else:
            return False


st = Solution()
result = st.judgeCircle("RLUDR")
print(result)
