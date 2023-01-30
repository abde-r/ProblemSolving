class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t=[]
        for i in title.split(' '):
            if len(i)>2:
                t.append(i.capitalize())
            else:
                t.append(i.lower())
        return ' '.join(t)

