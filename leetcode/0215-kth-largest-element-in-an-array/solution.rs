impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut begin = -10000;
        let mut end = 10000;
        while begin < end {
            let mid = (begin + end + 1) / 2;
            if nums.iter().filter(|&n| n >= &mid).count() < k as usize {
                end = mid - 1;
            } else {
                begin = mid;
            }
        }
        begin 
    }
}
