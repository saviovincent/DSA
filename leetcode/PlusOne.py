class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # str1 = ""
        # for i in digits:
        #     str1 += str(i)
        #
        # int_val = int(str1)
        # int_val = int_val+1
        #
        # str2 = str(int_val)
        #
        # final_list = []
        #
        # for i in str2:
        #     final_list.append(int(i))
        #
        # return final_list

        sum = carry = 1
        for i in range(len(digits) - 1, -1, -1):
            no = digits[i]
            sum = carry + no
            if sum > 9:
                carry = 1
                digits[i] = sum - 10
            else:
                carry = 0
                digits[i] += 1
                break
        if carry == 1:
            return [1] + digits
        return digits


if __name__ == '__main__':
    soln = Solution()
    print(soln.plusOne([9]))
