impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let minutes = minutes as usize;
        let satisfied_no_tech : i32 = customers.iter().zip(grumpy.iter()).map(|(&c, &g)| if g == 0 { c } else {0}).sum();
        let mut add_satisfied : i32 = customers.iter().zip(grumpy.iter()).take(minutes).map(|(&c, &g)| if g == 1 { c} else {0}).sum();
        let mut max_add_satisfied = add_satisfied;
        for i in minutes..customers.len() {
            if grumpy[i - minutes] == 1 {
                add_satisfied -= customers[i - minutes];
            }
            if grumpy[i] == 1 {
                add_satisfied += customers[i];
            }
            max_add_satisfied = std::cmp::max(max_add_satisfied, add_satisfied);
        }
        satisfied_no_tech + max_add_satisfied
        
    }
}
