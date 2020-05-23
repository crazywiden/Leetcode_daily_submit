/*
764. Largest Plus Sign
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.
*/
// simple dp
// time complexity -- O(N^2)
// Runtime: 284 ms, faster than 20.00% of Go online submissions for Largest Plus Sign.
// Memory Usage: 33.1 MB, less than 100.00% of Go online submissions for Largest Plus Sign.
func orderOfLargestPlusSign(N int, mines [][]int) int {
    grid := make([][]bool, N)
    for i:=0;i<N;i++{
        grid[i] = make([]bool, N)
    }
    for i:=0;i<N;i++{
        for j:=0;j<N;j++{
            grid[i][j] = true
        }
    }
    for i:=0;i<len(mines);i++{
        x, y := mines[i][0], mines[i][1]
        grid[x][y] = false
    }
    
    search := make([][][]int, N)
    for i:=0;i<N;i++{
        search[i] = make([][]int, N)
        for j := range search[i]{
            search[i][j] = []int{0,0,0,0}
        }
    }
    
    for i:=0;i<N;i++{
        if grid[i][0]{
            search[i][0][0] = 1
        }
        if grid[0][i]{
            search[0][i][1] = 1
        }
        if grid[i][N-1]{
            search[i][N-1][2] = 1
        }
        if grid[N-1][i]{
            search[N-1][i][3] = 1
        }
    }
    //fmt.Println(search)
    //fmt.Println(grid)
    res := 0
    for i:=0;i<N;i++{
        for j:=0;j<N;j++{
            if grid[i][j]{
                res = 1
                break
            }
        }
    }
    
    
    // from left and above
    for i:=1;i<N-1;i++{
        for j:=1;j<N-1;j++{
            if !grid[i][j]{
                continue
            }
            search[i][j][0] = search[i][j-1][0] + 1
            search[i][j][1] = search[i-1][j][1] + 1
        }
    }
    
    // from right and below
    for i:=N-2;i>0;i--{
        for j:=N-2;j>0;j--{
            if !grid[i][j]{
                continue
            }
            search[i][j][2] = search[i][j+1][2] + 1
            search[i][j][3] = search[i+1][j][3] + 1
        }
    }
    
    for i:=0;i<N;i++{
        for j:=0;j<N;j++{
            curr_res := MinOf(search[i][j])
            if curr_res == 0{
                continue
            }
            res = Max(res, curr_res)
        }
    }
    
    return res
}

func Max(x, y int) int{
    if x>y{
        return x
    }
    return y
}
func MinOf(vars []int) int {
    min := vars[0]
    for _, i := range vars {
        if min > i {
            min = i
        }
    }

    return min
}