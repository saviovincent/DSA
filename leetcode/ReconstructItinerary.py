class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from_ = {}
        to_ = {}
        start = None
        itinery = []
        for i in tickets:
            if i[0] not in from_:
                from_[i[0]]= i[1]
                to_[i[1]] = i[0]

        for i in from_:
            if i not in to_:
                start = i
                break

        itinery.append(start)
        try:
            while start:
                itinery.append(from_[start])
                start = from_[start]
        except Exception as e:
            pass

        return itinery

if __name__ == '__main__':
    soln= Solution()
    print(soln.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))