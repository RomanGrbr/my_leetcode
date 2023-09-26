package main

import "fmt"

func main() {
	nums := []int{3, 2, 3}
	t := 6
	var result = twoSum(nums, t)
	fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
    first := 0
	for first < len(nums) - 1 {
		for second := first + 1; second < len(nums); second++{
			if nums[first] + nums[second] == target{
				return []int{first, second}
			}
		}
		first++
	}
	return nil
}
