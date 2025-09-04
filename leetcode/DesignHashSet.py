class MyHashSet(object):

    def __init__(self):
        self.my_set = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not key in self.my_set:
            self.my_set.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.my_set:
            self.my_set.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """

        return key in self.my_set


if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.remove(2)
    print(obj.contains(1))
