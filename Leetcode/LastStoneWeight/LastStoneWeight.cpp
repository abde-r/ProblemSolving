int lastStoneWeight(vector<int>& stones)
{
        while (stones.size() > 1)
        {
            sort(stones.begin(), stones.end());
            if (stones[stones.size()-1] == stones[stones.size()-2])
                stones.pop_back();
            else if (stones[stones.size()-1] > stones[stones.size()-2])
                stones[stones.size()-2] = stones[stones.size()-1]-stones[stones.size()-2];
            else
                stones[stones.size()-2] = stones[stones.size()-2]-stones[stones.size()-1];
            stones.pop_back();
        }
        if (!stones.size())
            return 0;
        return stones[0];
}
