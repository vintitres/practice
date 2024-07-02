use std::collections::HashMap;
impl Solution {
    fn count_hash_map(nums: &Vec<i32>) -> HashMap<i32, usize> {
        let mut map = HashMap::new();
        for &n in nums {
            map.entry(n).and_modify(|c| *c += 1).or_insert_with(|| 1);
        }
        map
    }
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let nums1m = Self::count_hash_map(&nums1);
        let nums2m = Self::count_hash_map(&nums2);
        let mut intersection = vec![];
        for (num, count) in nums1m {
            if let Some(&count2) = nums2m.get(&num) {
                //println!("{} {}", count, count2);
                intersection.resize(intersection.len() + std::cmp::min(count,count2), num);
            }
        }
        intersection
        
    }
}
