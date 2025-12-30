class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        if(expression==""):
            return[]
        grp=[[]]
        lvl=0
        for i,j in enumerate(expression):
            # print(j)
            if j=="{":
                if lvl==0:
                    start=i+1
                lvl+=1
            elif j=="}":
                lvl-=1
                if lvl==0:
                    grp[-1].append(self.braceExpansionII(expression[start:i]))
            elif j=="," and lvl==0:
                grp.append([])
            elif lvl==0:
                grp[-1].append([j])
        uni=set()
        #cartesian preduct
        for g in grp: 
            uni |=set(map(''.join,itertools.product(*g)))
        return sorted(uni)
