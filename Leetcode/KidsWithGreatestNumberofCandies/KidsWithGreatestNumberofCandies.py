def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        t=[]
        _max = max(candies)
        for i in candies:
            if int(i)+extraCandies >= _max:
                t.append(True)
            else:
                t.append(False)
        return t

