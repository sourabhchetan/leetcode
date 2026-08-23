class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of '?' -> Alice makes the last move
        # and can always make the sums unequal.
        if (left_q + right_q) % 2 == 1:
            return True

        # If one side has more '?' than the other, the player
        # who controls those extra positions can force a difference.
        q_diff = left_q - right_q
        sum_diff = left_sum - right_sum

        # Bob can force equality only in this exact situation.
        return sum_diff != -9 * q_diff // 2
