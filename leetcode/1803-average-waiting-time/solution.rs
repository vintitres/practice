impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut total_wait_time : i64= 0;
        let mut chef_free : i64 = 0;
        for (arrival, time) in customers.iter().map(|c| (c[0] as i64, c[1] as i64)) {
            chef_free = std::cmp::max(chef_free, arrival) + time;
            total_wait_time += chef_free - arrival;
        }
        total_wait_time as f64 / customers.len() as f64
        
    }
}
