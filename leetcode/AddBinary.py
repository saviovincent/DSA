class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) > len(b):
            ltr = len(a)
        else:
            ltr = len(b)

        final_str = ""

        for i in range(ltr-1, -1, -1):
            temp = 0

            if a[i] == b[i] and a[i] == 0 and temp == 0:
                final_str += '0'

            elif a[i] == b[i] and i == 1 and temp == 0:
                final_str += '1'

            elif a[i] == b[i] and i == 0 and temp == 1:
                final_str += '1'

            elif a[i] == b[i] and i == 1 and temp == 1:
                final_str += '1'

