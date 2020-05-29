/*
474. Ones and Zeroes
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".


be careful about the difference in Golang between rune(character) and string
Runtime: 28 ms, faster than 78.26% of Go online submissions for Ones and Zeroes.
Memory Usage: 3.5 MB, less than 100.00% of Go online submissions for Ones and Zeroes.
*/
func findMaxForm(strs []string, m int, n int) int {
    dp := make([][]int, m+1)
    for i:=0; i<m+1; i++{
        dp[i] = make([]int, n+1)
    }
    
    for _, s := range strs{
        // fmt.Println(reflect.TypeOf(s))
        one, zero := get_one_zero(s)
        // fmt.Println(one, zero)
        if one > n || zero > m{
            continue
        }
        for i:=m; i>=zero; i--{
            for j:=n; j>=one; j--{
                dp[i][j] = MaxInt(dp[i][j], dp[i-zero][j-one] + 1)
            }
        }
    }
    return dp[m][n]
}

func MaxInt(x, y int) int{
    if x > y{
        return x
    }
    return y
}

func get_one_zero(s string)(int, int){
    one, zero := 0, 0
    for i:=0; i<len(s); i++{
        if string(s[i]) == "0"{
            zero += 1
        } else {
            one += 1
        }
    }
    return one, zero
}