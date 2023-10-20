/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let min = strs[0]
    for (let i=1; i<strs.length; i++){
        if (min.length > strs[i].length){
            min = strs[i]
        }
    }
    // i = strs.indexOf(min)
    strs.splice(strs.indexOf(min), 1)
    let i = min.length
    while (i !==0){
        let flag = true
        for (let word=0; word<strs.length; word++){
            if (strs[word][0, i].includes(min[0, i], 0)){
                flag = false
                break
            }
        } if( flag == true){
            return min[0, i]
        }
        i--
    }
};

console.log(longestCommonPrefix(["flower","flow","flight"])) // "fl"
console.log(longestCommonPrefix(["dog","racecar","car"])) // ""