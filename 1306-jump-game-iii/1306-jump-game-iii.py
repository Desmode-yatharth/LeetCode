class Solution:
    from collections import deque
    def canReach(self, arr: list[int], start: int) -> bool:

        visit = set()
        l_r,r_r = start - arr[start],start + arr[start]
        if l_r < 0 : l_r = "U"
        if r_r > len(arr) - 1 : r_r = "U"
        q = deque([(start,l_r,r_r)])
        
        while q:

            curr_idx,left_r,right_r = q.popleft()

            
            if arr[curr_idx] == 0 : return True
            if (curr_idx,left_r,right_r) in visit : continue
            
            

            neigs = [left_r,right_r]
            print(neigs)
            if left_r == "U" : neigs.remove(left_r)
            if right_r == "U" : neigs.remove(right_r)
            
            visit.add((curr_idx,left_r,right_r))

            for idx in neigs :
                new_left_r,new_right_r = idx - arr[idx],idx + arr[idx]
                
                if new_left_r < 0 : new_left_r = "U"
                if new_right_r > len(arr) - 1 : new_right_r = "U"

                if (idx,new_left_r,new_right_r) not in visit :
                    q.append((idx,new_left_r,new_right_r))
                    


        return False
        
        
        