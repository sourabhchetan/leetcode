class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        sort(coins.begin(), coins.end());

        // Remove redundant coins
        vector<long long> c;

        for (int x : coins) {
            bool redundant = false;

            for (long long y : c) {
                if (x % y == 0) {
                    redundant = true;
                    break;
                }
            }

            if (!redundant)
                c.push_back(x);
        }

        int n = c.size();

        // Count how many valid amounts <= x
        auto count = [&](long long x) {
            long long total = 0;

            for (int mask = 1; mask < (1 << n); mask++) {
                long long lcm = 1;
                int bits = 0;
                bool tooLarge = false;

                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        bits++;

                        long long g = gcd(lcm, c[i]);

                        // Avoid overflow
                        lcm = lcm / g;

                        if (lcm > x / c[i]) {
                            tooLarge = true;
                            break;
                        }

                        lcm *= c[i];
                    }
                }

                if (tooLarge || lcm > x)
                    continue;

                if (bits % 2 == 1)
                    total += x / lcm;
                else
                    total -= x / lcm;
            }

            return total;
        };

        // Binary search
        long long left = 1;
        long long right = c[0] * (long long)k;

        while (left < right) {
            long long mid = left + (right - left) / 2;

            if (count(mid) >= k)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};
