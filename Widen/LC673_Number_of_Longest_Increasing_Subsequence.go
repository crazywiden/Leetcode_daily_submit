/*
673. Number of Longest Increasing Subsequence
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

time complexity -- O(N^2)
Runtime: 8 ms, faster than 100.00% of Go online submissions for Number of Longest Increasing Subsequence.
Memory Usage: 3.4 MB, less than 100.00% of Go online submissions for Number of Longest Increasing Subsequence.
*/

func findNumberOfLIS(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    N := len(nums)
    length := make([]int, N)
    count := make([]int, N)
    for i:=0;i<N;i++{
        count[i] = 1
        for j:=i-1;j>=0;j--{
            if nums[j] >= nums[i]{
                continue
            }
            curr_len := length[j] + 1
            if curr_len == length[i]{
                count[i] += count[j]
            } else if curr_len > length[i] {
                length[i] = curr_len
                count[i] = count[j]
            } 
        }
    }
    res := 0
    max_len := MaxInt(length)
    for i:=0 ; i<N ; i++{
        if length[i] == max_len{
            res += count[i]
        }
    }
    return res
}

func MaxInt(arr []int) int{
    res := arr[0]
    for i:=0; i<len(arr) ; i++{
        if arr[i] > res{
            res = arr[i]
        }
    }
    return res
}