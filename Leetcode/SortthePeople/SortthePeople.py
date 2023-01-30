class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        r = []
        for i in range(0,len(names)):
            r.append([heights[i], names[i]])
        r = sorted(r, reverse=True)
        s=[]
        for i in range(0, len(r)):
            s.append(r[i][1])
        return s

