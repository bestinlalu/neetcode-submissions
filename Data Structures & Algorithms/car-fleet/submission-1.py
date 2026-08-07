class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        pairs = sorted([(position[i], ((target - position[i]) / speed[i])) for i in range(len(position))], reverse = True)
        
        # print(pairs)
        last_time = 0

        for p, t in pairs:
            if t > last_time:
                fleet += 1
                last_time = t

        return fleet
        
