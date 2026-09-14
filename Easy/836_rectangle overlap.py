class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        # Find the intersection boundaries
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])

        # Intersection must have positive width and height
        return left < right and bottom < top
