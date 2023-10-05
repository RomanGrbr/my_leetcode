/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let ROMAN = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }
    let result = 0
    let index = 1
    let len_s = s.length
    if (len_s === 1){
        return ROMAN[s];
    };
    while (index < len_s){
        if (ROMAN[s[index - 1]] >= ROMAN[s[index]]){
            result += ROMAN[s[index - 1]]
            index++
        } else {
            result += ROMAN[s[index]] - ROMAN[s[index - 1]]
            index += 2
        };
    };
    if (index == len_s){
        result += ROMAN[s[index - 1]]
        return result
    };
    return result
};

console.log(romanToInt('MDCXCV'))
console.log(romanToInt('III'))
console.log(romanToInt('XIV'))
console.log(romanToInt('MCMXCIV'))
