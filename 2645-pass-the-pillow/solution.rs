impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        match time % (2 * n - 2) {
            t if t < n => t + 1,
            t => n - (t + 1 - n)
        } 
    }
}

// n = 3
// 0 -> 0
// 1 -> 1
// 2 -> 2
// 3 -> 1
// 4 -> 0
