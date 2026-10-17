
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(
            enumerate(nums),
            key=lambda p: (
                sum(int(d) for d in str(p[1])),
                p[1]
            )
        )

        v = set()
        swaps = 0
        n = len(nums)

        for i in range(n):
            if i in v or arr[i][0] == i:
                continue

            cycle_len = 0
            j = i

            while j not in v:
                v.add(j)
                j = arr[j][0]
                cycle_len += 1

            swaps += cycle_len - 1

        return swaps

        