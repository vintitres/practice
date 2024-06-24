impl Solution {
    pub fn min_k_bit_flips(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut flips = 0;
        let k = k as usize;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                flips += 1;
                if i + k > nums.len() {
                    return -1;
                }
                for j in i..i + k {
                    nums[j] = if nums[j] == 1 {0} else {1};
                }
            }
            //println!("{} {:?}", &i, &nums);
        }
        flips
        
    }
}
