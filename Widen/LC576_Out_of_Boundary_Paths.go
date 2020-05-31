/*
576. Out of Boundary Paths
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, 
you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). 
However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 109 + 7.


Runtime: 0 ms, faster than 100.00% of Go online submissions for Out of Boundary Paths.
Memory Usage: 5.3 MB, less than 100.00% of Go online submissions for Out of Boundary Paths.
*/
import "math"
func findPaths(m int, n int, N int, i int, j int) int {
    MAX_INT := int(math.Pow10(9) + 7)
    dp := make([][][]int, N+1)
    for row:=0; row<N+1; row++{
        dp[row] = make([][]int, m)
        for col:=0; col<m; col++{
            dp[row][col] = make([]int, n)
        }
    }
    
    for step:=1; step<=N; step++{
        for row:=0; row<m; row++ {
            for col:=0; col<n; col++{
                if row == 0{
                    dp[step][row][col] += 1
                } else {
                    dp[step][row][col] += dp[step-1][row-1][col]
                }
                
                if row == m-1{
                    dp[step][row][col] += 1
                } else {
                    dp[step][row][col] += dp[step-1][row+1][col]
                }
                
                if col == 0{
                    dp[step][row][col] += 1
                } else {
                    dp[step][row][col] += dp[step-1][row][col-1]
                }
                
                if col == n-1 {
                    dp[step][row][col] += 1
                } else {
                    dp[step][row][col] += dp[step-1][row][col+1]
                }
                dp[step][row][col] = dp[step][row][col] % MAX_INT
            }
        }
    } 
    return dp[N][i][j] % MAX_INT
}