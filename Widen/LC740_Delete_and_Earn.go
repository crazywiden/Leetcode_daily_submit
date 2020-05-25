/*
740. Delete and Earn
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
*/


// Runtime: 4 ms, faster than 100.00% of Go online submissions for Delete and Earn.
// Memory Usage: 3.6 MB, less than 100.00% of Go online submissions for Delete and Earn.
import "sort"
func deleteAndEarn(nums []int) int {
    freq := make(map[int]int)
    for _, val:= range nums{
        if _, ok := freq[val]; ok{
            freq[val] += val
        } else {
            freq[val] = val
        }
    }

    keys := make([]int, 0, len(freq))
    for key := range freq{
        keys = append(keys, key)
    }
    sort.Ints(keys)
    prev, curr := 0, 0
    for _, key := range keys{
        if _, ok := freq[key-1]; ok{
            a := curr
            curr = Max_Ints(curr, prev + freq[key])
            prev = a
        } else {
            prev = curr
            curr = freq[key] + curr
        }
    }
    return Max_Ints(curr, prev)
}

func Max_Ints(x, y int) int{
    if x > y{
        return x
    }
    return y
}