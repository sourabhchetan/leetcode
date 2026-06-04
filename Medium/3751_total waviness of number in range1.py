class Solution:
    def totalWaviness(self, num1, num2):
        def waviness(num):
            s = str(num)

            if len(s) < 3:
                return 0

            count = 0

            for i in range(1, len(s) - 1):
                left = int(s[i - 1])
                mid = int(s[i])
                right = int(s[i + 1])

                if mid > left and mid > right:  # peak
                    count += 1
                elif mid < left and mid < right:  # valley
                    count += 1

            return count

        total = 0

        for num in range(num1, num2 + 1):
            total += waviness(num)

        return total