class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = defaultdict(list)
        crsorder = []
        visited = set()

        def dfs(crs) -> bool:
            if crs in visited:
                return False
            if not preMap[crs] and crs not in crsorder:
                crsorder.append(crs)
                return True
            if not preMap[crs]:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            if crs not in crsorder:
                crsorder.append(crs)
            return True

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        for crs in range(numCourses):
            if not preMap[crs]:
                preMap[crs] = []

        for crs, pre in prerequisites:
            if not dfs(crs):
                return []
                
        for crs in preMap.keys():
            if crs not in crsorder:
                crsorder.append(crs)
        return crsorder