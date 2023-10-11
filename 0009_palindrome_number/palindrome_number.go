package main

import (
    "fmt"
    "strings"
    "strconv"
)

func isPalindrome(x int) bool {
    original_array := strings.Split(strconv.Itoa(x), "")
    for i := 0; i < len(original_array); i++ {
        if original_array[i] != original_array[len(original_array) - i - 1] {
            return false
        }
    }
    return true
}

func main() {
	num := -121
	var result = isPalindrome(num)
	fmt.Println(result)
}
