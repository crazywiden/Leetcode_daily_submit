/*
646. Maximum Length of Pair Chain
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
*/


type Pair struct {x, y int}

type PairSorter []Pair

func (ps PairSorter) Len() int{
    return len(ps)
}

func (ps PairSorter) Swap(i, j int){
    ps[i], ps[j] = ps[j], ps[i]
}

func (ps PairSorter) Less(i, j int) bool{
    return ps[i].y < ps[j].y
}

func findLongestChain(pairs [][]int) int {
    pair_arr := make([]Pair, 0, len(pairs))
    for _, p := range pairs{
        pair_arr = append(pair_arr, Pair{p[0], p[1]})
    }
    ps := PairSorter(pair_arr)
    sort.Sort(ps)
    res := 0
    curr := math.MinInt32
    for _, p := range ps{
        if curr >= p.x{
            continue
        } else {
            curr = p.y
            res += 1
        }
    }
    return res
}