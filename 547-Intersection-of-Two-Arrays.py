class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        set1 = set()
        for num in nums1:
            if num not in set1:
                set1.add(num)
        set2 = set()
        for num in nums2:
            if num in set1 and num not in set2:
                set2.add(num)
        return list(set2)
