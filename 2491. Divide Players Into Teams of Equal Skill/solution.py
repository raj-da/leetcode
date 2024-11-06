class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teamSkill = skill[-1] + skill[0]
        chemistry = 0

        l, r = 0, len(skill)-1
        while l < r:

            if skill[l] + skill[r] != teamSkill:
                return -1
            
            chemistry += (skill[l] * skill[r])
            l += 1
            r -= 1

        return chemistry