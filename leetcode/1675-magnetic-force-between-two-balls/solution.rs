impl Solution {
    fn check_force(position: &Vec<i32>, m: i32, force: i32) -> bool {
        let mut last_position = -force;
        let mut to_place = m;
        for i in 0..position.len() {
            if position[i] - force >= last_position {
                last_position = position[i];
                to_place -= 1;
                if to_place == 0 {
                    return true;
                }
            }
        } 
        false
    }
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        let mut position = position.clone();
        position.sort();
        let mut begin = 0;
        let mut end = *position.last().unwrap();
        while begin < end {
            let mid = (begin + end + 1) / 2;
            if (Self::check_force(&position, m, mid)) {
                begin = mid;
            } else {
                end = mid - 1;
            }
        }
        end
    }
}
