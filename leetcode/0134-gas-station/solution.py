class Solution:
    # so bad implementation
    def consolidate_sign(l: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        consolidated = []
        last_gas = 0
        last_pos = 0
        for gas, pos in l:
            #print(last_gas, last_pos, gas, pos)
            #print(consolidated)
            if (last_gas >= 0 and gas >= 0) or (last_gas < 0 and gas < 0):
                last_gas += gas
            else:
                consolidated += [(last_gas, last_pos)]
                last_gas = gas
                last_pos = pos
        if last_gas != 0:
            consolidated += [(last_gas, last_pos)]
        #print(consolidated, last_gas)
        if len(consolidated) > 1 and ((consolidated[0][0] <= 0 and consolidated[-1][0] <= 0) or (consolidated[0][0] >= 0 and consolidated[-1][0] >= 0)):
            consolidated[0] = (consolidated[0][0] + consolidated[-1][0], consolidated[-1][1])
            consolidated = consolidated[:-1]
        #print(consolidated)
        return consolidated
    
    def cons_positive(l: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not l:
            return []
        last_gas = l[0][0]
        last_pos = l[0][1]
        ret = []
        for gas, pos in l[1:]:
            if last_gas >= 0 and last_gas + gas >= 0:
                last_gas += gas
            else: 
                ret += [(last_gas, last_pos)]
                last_gas = gas
                last_pos = pos
        ret += [(last_gas, last_pos)]
        #print(ret, last_gas)
        if len(ret) > 1 and ret[-1][0] > 0 and ret[0][0] + ret[-1][0] >= 0:
            ret[0] = (ret[0][0] + ret[-1][0], ret[-1][1])
            ret = ret[:-1]
        return ret
        


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1   2  3 4 5
        # 3   4  5 1 2
        # -2 -2 -2 3 3
        # -6 6

        # -2 -2 1 -2 2 3
        # -4 1 -2 5
        # -5 5

        
        gas_here = [0] * len(gas)
        for i in range(len(gas)):
            gas_here[i] = (gas[i] - cost[i], i)
        print(gas_here)
        last_len = len(gas_here)
        while len(gas_here) > 2:
            gas_here = Solution.consolidate_sign(gas_here)
            #print(gas_here)
            #print("!")
            gas_here = Solution.cons_positive(gas_here)
            #print(gas_here)
            if len(gas_here) == last_len:
                return -1
            last_len = len(gas_here)
        
        if len(gas_here) == 2:
            if gas_here[0][0] + gas_here[1][0] >= 0:
                if gas_here[0][0] >= 0:
                    return gas_here[0][1]
                else:
                    return gas_here[1][1]
            else:
                return -1
        elif len(gas_here) == 1:
            if gas_here[0][0] >= 0:
                return gas_here[0][1]
            else:
                return -1
        else:
            return -1
        


                
