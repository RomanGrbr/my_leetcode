/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let first = 0;
    while (first < nums.length - 1){
        for (second = first + 1; second < nums.length; second++){
            if (nums[first] + nums[second] === target){
                return [first, second];
            };
        };
        first++
    }
};

console.log(twoSum([3, 2, 3], 6))