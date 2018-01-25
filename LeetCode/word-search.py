class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word and not board:
            return False
        
        used = []
        return self.helper(board, word, used, None)
    
    def helper(self, board, word, used, cur):
        if not word:
            return True
        
        if not cur:
            # Find all word[0]
            found = False
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if found:
                        return True
                    if word[0] == board[i][j]:
                        found = found or self.helper(board, word[1:], used+[[i,j]], [i,j])
            return found
        else:
            # Check all spots by cur for word[0]
            found = False
            r = cur[0]
            c = cur[1]
            # up
            if r > 0 and [r-1,c] not in used and board[r-1][c] == word[0]:
                found = found or self.helper(board, word[1:], used+[[r-1,c]], [r-1,c])
            # down
            if r < len(board) - 1 and [r+1,c] not in used and board[r+1][c] == word[0]:
                found = found or self.helper(board, word[1:], used+[[r+1,c]], [r+1,c])
            # left
            if c > 0 and [r,c-1] not in used and board[r][c-1] == word[0]:
                found = found or self.helper(board, word[1:], used+[[r,c-1]], [r,c-1])
            # right
            if c < len(board[0]) - 1 and [r,c+1] not in used and board[r][c+1] == word[0]:
                found = found or self.helper(board, word[1:], used+[[r,c+1]], [r,c+1])
            
            return found
        