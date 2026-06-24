class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        offSet = (minutes)/60 * 5
        hourMinutes = (hour if hour != 12 else 0) * 5

        minInBetween = abs(hourMinutes - minutes) + (offSet if hourMinutes >= minutes else -offSet)

        res =  abs((minInBetween/60) * 360)
        return min(res, 360 - res)
