import "strconv"

func isValidSudoku(board [][]byte) bool {
	N := len(board)
	var row, col, box []map[int]bool
	// fmt.Println(row)
	for i := 0; i < N; i++ {
		row = append(row, make(map[int]bool))
		col = append(col, make(map[int]bool))
		box = append(box, make(map[int]bool))
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if board[i][j] == '.' {
				continue
			}
			n, _ := strconv.Atoi(string(board[i][j]))
			// n := int(board[i][j]) - '0'
			if row[i][n] || col[j][n] || box[(i/3)*3+j/3][n] {
				return false
			}
			row[i][n] = true
			col[j][n] = true
			box[(i/3)*3+j/3][n] = true
		}
	}
	// fmt.Println(row)
	return true
}