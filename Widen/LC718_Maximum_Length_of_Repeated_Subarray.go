/*
718. Maximum Length of Repeated Subarray
718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

Runtime: 60 ms, faster than 77.19% of Go online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 16.2 MB, less than 100.00% of Go online submissions for Maximum Length of Repeated Subarray.
*/
func findLength(A []int, B []int) int {
    n_A, n_B := len(A), len(B)
    dp := make([][]int, n_A)
    for i:=0; i<n_A; i++{
        dp[i] = make([]int, n_B)
    }
    for i:= 0; i<n_A; i++{
        if B[n_B-1] == A[i]{
            dp[i][n_B-1] = 1
        }
    }
    
    for i:=0; i<n_B; i++{
        if A[n_A-1] == B[i]{
            dp[n_A-1][i] = 1
        }
    }
    res := 0
    for row:=n_A-2; row>=0; row--{
        for col:=n_B-2; col>=0; col--{
            if A[row] != B[col]{
                continue
            } else {
                dp[row][col] = 1 + dp[row+1][col+1]
            }
            res = MaxInt(res, dp[row][col])
        }
    }
    return res
}

func MaxInt(x, y int) int{
    if x > y{
        return x
    }
    return y
}