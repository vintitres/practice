impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut end = 0;
        let mut begin = 0;
        let mut odd = 0;
        let mut nice = 0;
        while true {
            if odd == k {
                let right_start = end;
                while end < nums.len() && nums[end] % 2 == 0 {
                    end += 1;
                }
                let left_start = begin;
                while begin < nums.len() && nums[begin] % 2 == 0 {
                    begin += 1;
                }
                nice += (begin - left_start + 1) as i32* (end - right_start + 1) as i32;
                // println!("{} {} {}", nice, begin, end);
            }
            if begin == nums.len() {
                break;
            }
            if odd <= k && end < nums.len() {
                odd += if nums[end] % 2 == 1 {1} else {0};
                end += 1;
            } else {
                odd -= if nums[begin] % 2 == 1 {1} else {0};
                begin += 1;
            }

        }
        nice
    }
}
