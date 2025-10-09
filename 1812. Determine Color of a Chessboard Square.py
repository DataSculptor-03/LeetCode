class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        col = ord(coordinates[0]) - ord('a') + 1  
        row = int(coordinates[1])               

        return (col + row) % 2 == 1
