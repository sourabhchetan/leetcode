class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Closest point on the rectangle to the circle center
        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2))

        # Check whether that point is inside/on the circle
        dx = x - xCenter
        dy = y - yCenter

        return dx * dx + dy * dy <= radius * radius
