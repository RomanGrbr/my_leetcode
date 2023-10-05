package main

import "fmt"

func romanToInt(s string) int {
    roman := map[string]int{
		"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
	}
	result := 0
    index := 1
    len_s := len(s)
	if len_s == 1 {
        return roman[s];
    };
	for index < len_s{
        if roman[string(s[index - 1])] >= roman[string(s[index])]{
            result += roman[string(s[index - 1])]
            index++
        } else {
            result += roman[string(s[index])] - roman[string(s[index - 1])]
            index += 2
        };
    };
    if index == len_s{
        result += roman[string(s[index - 1])]
        return result
    };
	return result
}

func main() {
	fmt.Println(romanToInt("MDCXCV"))
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("XIV"))
	fmt.Println(romanToInt("MCMXCIV"))
}