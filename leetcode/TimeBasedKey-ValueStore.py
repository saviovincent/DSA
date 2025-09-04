from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        self.data[key].append((timestamp, value))
        print(self.data)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        for i in self.data[key]:
            if timestamp == i[0]:
                return i[1]
            elif timestamp
        return ""


if __name__ == '__main__':
    obj = TimeMap()
    print(obj.set("foo", "bar", 1))
    print(obj.get("foo", 1))
