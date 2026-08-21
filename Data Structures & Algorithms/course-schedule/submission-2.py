class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        visited = set()

        for course in prerequisites:
            preMap[course[0]].append(course[1])

        def dfs(course) -> bool:
            if course in visited:
                return False
            if not preMap[course]:
                return True
            visited.add(course)
            
            for c in preMap[course]:
                if not dfs(c):
                    return False
            preMap[course] = []
            visited.remove(course)
            return True
        
        for crs, prev in prerequisites:
            if not dfs(crs):
                return False
        return True


        