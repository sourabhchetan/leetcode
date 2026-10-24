class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))

        return max(0, end - start + 1)
