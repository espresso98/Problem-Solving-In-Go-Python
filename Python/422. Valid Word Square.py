# Given an array of strings words, return true if it forms a valid word square.
# A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

def validWordSquare(self, words: List[str]) -> bool:
        # Solution 1: Time Complexity:  O(mn),  Space Complexity: O(1)
        W = words  
        for i in range(len(W)):
            for j in range(len(W[i])):
                if j >= len(W) or i >= len(W[j]) or W[i][j] != W[j][i]:
                    return False
        return True
        
        # Solution 2: Time Complexity:  O(mn),  Space Complexity: O(mn)
        square_mat = []
        max_word_len = len(max(words, key=len))

        for word in words:
            word_len = len(word)
            if  word_len != max_word_len:
                square_mat.append(list(word) + ['.'] * (max_word_len - word_len))
            else:
                square_mat.append(list(word))
        
        M, N = len(square_mat), len(square_mat[0])
        transposed_mat = [[square_mat[r][c] for r in range(M)] for c in range(N)]
        return square_mat == transposed_mat