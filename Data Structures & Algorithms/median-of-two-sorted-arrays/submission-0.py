class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total = len(nums1) + len(nums2)
        half = total // 2


        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A) - 1
        while True:
            mid1 = (left + right) // 2 #A
            mid2 = half - mid1 - 2 #B

            Aleft = A[mid1] if mid1 >= 0 else float('-inf')
            Aright = A[mid1 + 1] if mid1 + 1 < len(A) else float('inf')

            Bleft = B[mid2] if mid2 >= 0 else float('-inf')
            Bright = B[mid2 + 1] if mid2 + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = mid1 - 1
            else:
                left = mid1 + 1



