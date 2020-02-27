"""
302. Smallest Rectangle Enclosing Black Pixels
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""



# brutal force 
# time complexity -- O(N^2)
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n_row, n_col = len(image), len(image[0])
        left, right = n_col, -1
        top, down = n_row, -1
        for i in range(n_row):
            for j in range(n_col):
                if image[i][j] == "1":
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    down = max(down, i)
        return (right-left+1) * (down-top+1)

# binary search 
# brilliant idea! And finally make sense why do we need x and y
# time complexity -- O(nlog m + m log n)
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n_row, n_col = len(image), len(image[0])
        left = self.search_row(image, 0, y, True)
        right = self.search_row(image, y, n_col, False)
        top = self.search_col(image, 0, x, True)
        down = self.search_col(image, x, n_row, False)
        return (down-top) * (right-left)
    
    def search_row(self, image, left, right, is_black):
        while left < right:
            mid = (left+right)//2
            met_black = False
            for row in range(len(image)):
                if image[row][mid] == "1":
                    met_black = True
                    break
            if is_black:
                if met_black:
                    right = mid 
                else:
                    left = mid + 1 
            else:
                if met_black:
                    left = mid + 1 
                else:
                    right = mid 
        return right 
        
    def search_col(self, image, top, down, is_black):
        while top < down:
            mid = (top + down) // 2
            met_black = False
            for col in range(len(image[0])):
                if image[mid][col] == "1":
                    met_black = True
                    break
            if is_black:
                if met_black:
                    down = mid
                else:
                    top = mid + 1 
            else:
                if met_black:
                    top = mid + 1 
                else:
                    down = mid 
        return down


