impl Solution {
    // 1 2 3 4 5
    // 1 2 3 4
    pub fn find_the_winner(n: i32, k: i32) -> i32 {
        if n == 1 {
            1
        } else {
            (Self::find_the_winner(n - 1, k) + k - 1) % n + 1 
        }
    }
}
