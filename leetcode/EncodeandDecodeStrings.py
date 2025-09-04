class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for i in strs:
            length = len(i)
            ans += str(length) + "#" + i
        return ans

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        ans = []
        i = 0

        while i < len(s):

            count = ""
            while s[i] != "#":
                count += s[i]
                i+=1

            count = int(count)
            ans.append(s[i+1:i+1+count])
            i += count+1
        return ans



if __name__ == '__main__':
    codec = Codec()
    print(codec.encode(["Hello", "World"]))
    print(codec.decode("5#Hello5#World"))
    # codec.decode(codec.encode(["Hello","World"]))
