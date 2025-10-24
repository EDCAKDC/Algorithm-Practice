class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        res = ['']*len(score)
        for rank, (idx, val) in enumerate(sorted_scores, start=1):
            if rank==1:
                res[idx] =  "Gold Medal"
            elif rank==2:
                res[idx] =  "Silver Medal"
            elif rank==3:
                res[idx] =  "Bronze Medal"
            else:
                res[idx] =  str(rank)
        return res