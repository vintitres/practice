impl Solution {
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let mut city_roads = Vec::<usize>::new();
        city_roads.resize(n as usize, 0);
        for road in roads {
            city_roads[road[0] as usize] += 1;
            city_roads[road[1] as usize] += 1;
        }
        let mut indexes : Vec<usize> = (0..n as usize).collect();
        indexes.sort_by(|&i, &j| city_roads[i].partial_cmp(&city_roads[j]).unwrap());
        let mut importance = 0;
        for i in (0..n as usize).rev() {
            importance += (i as i64 + 1) * city_roads[indexes[i]] as i64;
        }
        importance
    }
}
