/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (first = 0; first < nums.length; first++) {
        for (second = first + 1; second < nums.length; second++) {
            if (nums[first] + nums[second] === target){
                return [first, second];
            };
        };
    };
}

console.log(twoSum([3, 2, 3], 6))