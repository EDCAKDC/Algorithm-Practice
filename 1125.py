class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        idx = {s: i for i, s in enumerate(req_skills)}
        p_mask = []
        for skills in people:
            mask = 0
            for s in skills:
                if s in idx:
                    mask |= 1 << idx[s]
            p_mask.append(mask)
        rep = {}
        for i, mi in enumerate(p_mask):
            if mi:
                rep.setdefault(mi, i)
        useful = [(i, mi) for mi, i in rep.items()]
        all = 1 << m
        dp = all * [None]
        dp[0] = []
        for i, mi in useful:
            cur = dp[:]
            for mask in range(all):
                if cur[mask] is None:
                    continue
                new = mask | mi
                cand = cur[mask] + [i]
                if dp[new] is None or len(cand) < len(dp[new]):
                    dp[new] = cand
        return dp[all-1]
