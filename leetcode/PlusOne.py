class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str1 = ""
        for i in digits:
            str1 += str(i)

        int_val = int(str1)
        int_val = int_val+1

        str2 = str(int_val)

        final_list = []

        for i in str2:
            final_list.append(int(i))

        return final_list
