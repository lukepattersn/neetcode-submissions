class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)

        #dfs: not visited yet, in curr dfs path (cycle)
        # fully processed (added to output)
        visit = set()
        cycle = set()
        output = []

        #track visited nodes, detect cycles
        def dfs(course):
            # if we encounter a course in curr path, we found a cycle
            if course in cycle:
                return False

            # if already processed, skip
            if course in visit:
                return True

            # add to current path
            cycle.add(course)

            # process all prereq first
            for pre in prereq[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visit.add(course)

            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output 