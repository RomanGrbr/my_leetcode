package main

import "fmt"


func twoSum(nums []int, target int) []int {
	for first := 0; first < len(nums); first++ {
		for second := first + 1; second < len(nums); second++ {
			if nums[first] + nums[second] == target{
				return []int{first, second}
			}
		}
	}
	return nil
}


func main() {
	nums := []int{3, 2, 3}
	t := 6
	var result = twoSum(nums, t)
	fmt.Println(result)
}
