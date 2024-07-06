impl Solution {
    pub fn min_difference(nums: Vec<i32>) -> i32 {
        let MOVES = 3;
        if nums.len() <= MOVES + 1 {
            return 0;
        }
        let mut nums = nums;
        nums.sort();
        let mut best = i32::MAX;
        for i in 0..=MOVES {
            best = std::cmp::min(best, nums[nums.len() - 1 - MOVES + i] - nums[i]);
        }
        best

    }
}
