use std::collections::BTreeSet;
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let mut nums_between = BTreeSet::<(i32, usize)>::new();
        let mut begin = 0;
        let mut end = 0;
        let mut max_len = 0;
        while begin < nums.len() {
            if begin == end {
                nums_between.insert((nums[end], end));
                end += 1;
            }
            let mut min = nums_between.first().unwrap().0;
            let mut max = nums_between.last().unwrap().0;
            //println!("beg{} end{} max{} min{}", begin, end, max, min);
            if max - min <= limit {
                //println!("ok{}", end - begin);
                max_len = std::cmp::max(max_len, end - begin);
            }
            if max - min <= limit && end < nums.len() {
                nums_between.insert((nums[end], end));
                end += 1;
            } else {
                nums_between.remove(&(nums[begin], begin));
                begin += 1;
            }
        }
        max_len as i32
    }
}
