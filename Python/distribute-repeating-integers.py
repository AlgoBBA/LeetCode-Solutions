# Time:  O(m * 3^m) 
# Space: O(2^m)

import collections


class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        total = (1<<len(quantity))-1
        requirement = [0]*(total+1)
        for mask in xrange(len(requirement)):  # Time: O(2^m)
            base = 1
            for i in xrange(len(quantity)):  # Time: O(m)
                if mask&base:
                    requirement[mask] += quantity[i];
                base <<= 1
        dp = [[0]*(total+1) for _ in xrange(2)]
        dp[0][0] = 1
        i = 0
        cnts = sorted(count.itervalues(), reverse=True)[:len(quantity)]
        for cnt in cnts:  # Time: O(m)
            dp[(i+1)%2] = [0]*(total+1)
            # Time: O(3^m), see https://cp-algorithms.com/algebra/all-submasks.html
            for mask in reversed(xrange(total+1)):
                dp[(i+1)%2][mask] |= dp[i%2][mask]
                sub_mask = mask
                while sub_mask > 0:
                    if requirement[sub_mask] <= cnt and dp[i%2][mask^sub_mask]:
                        dp[(i+1)%2][mask] = 1
                    sub_mask = (sub_mask-1)&mask
            i += 1
        return dp[len(cnts)%2][total]
