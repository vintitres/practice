impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut drunk = 0;
        let mut bottles = num_bottles;
        while bottles >= num_exchange {
            drunk += bottles / num_exchange * num_exchange;
            let left_over = bottles % num_exchange;
            bottles /= num_exchange;
            bottles += left_over;
        }
        drunk + bottles
    }
}
