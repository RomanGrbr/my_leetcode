/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let original_array = String(x).split('')
    for (let i=0; i<original_array.length; i++){
        if (original_array[i] !== original_array[original_array.length - i - 1]){
            return false
        }
    }
    return true
};

console.log(isPalindrome(121))
console.log(isPalindrome(123456))
console.log(isPalindrome(1234321))
console.log(isPalindrome(-121))