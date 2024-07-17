use rand::Rng;
use rand::rngs::ThreadRng;
use std::collections::HashMap;
use std::collections::hash_map::Entry;

struct RandomizedSet {
    set: Vec<i32>,
    pos: HashMap<i32, usize>,
    rng: ThreadRng,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        Self {set: Vec::new(), pos: HashMap::new(), rng: rand::thread_rng()}
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if let Entry::Vacant(e) = self.pos.entry(val) {
            self.set.push(val);
            e.insert(self.set.len() - 1);
            true
        } else {
            false
        }
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if let Entry::Occupied(e) = self.pos.entry(val) {
            let remove_index = *e.get();
            e.remove();
            //println!("remove {remove_index} {:?}", self.set);
            let last_val = self.set.pop().unwrap();
            if self.set.len() != remove_index {
                self.set[remove_index] = last_val;
                *self.pos.get_mut(&last_val).unwrap() = remove_index;
            }
            true
        } else {
            false
        }
    }
    
    fn get_random(&mut self) -> i32 {
        self.set[self.rng.gen::<usize>() % self.set.len()]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
