class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        r=nums1+nums2
        r.sort()
        n=len(r)
        if n%2==0:
            return (r[n//2-1]+r[n//2])/2.0
        else:
            return (r[n//2])