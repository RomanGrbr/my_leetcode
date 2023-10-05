/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let original_array = String(x).split('')
    let reversed_array = []
    original_array.forEach((element) => {
        reversed_array.unshift(element);
    });
    // return y == y.slice(-1)
    
    return y == reversed_array
};

console.log(isPalindrome(121))
console.log(isPalindrome(123456))
console.log(isPalindrome(1234321))
// console.log(romanToInt(-121))