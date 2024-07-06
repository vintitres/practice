impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        arr.iter().scan(0, |odd_count, &num| {
            if *odd_count == 3 {
                return None;
            }
            if (num % 2 == 1) {
                *odd_count += 1;
                if *odd_count == 3 {
                    return Some(Some(true));
                }
            } else {
                *odd_count = 0;
            }
            Some(None)
        }).flatten().count() == 1
    }
}
