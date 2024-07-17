use rand::Rng;
use rand::rngs::ThreadRng;
use std::collections::HashMap;
use std::collections::hash_map::Entry;

struct RandomizedSet {
    set: Vec<i32>,
    pos: HashMap<i32, usize>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        Self {set: Vec::new(), pos: HashMap::new()}
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
            self.set.swap_remove(remove_index);
            if self.set.len() != remove_index {
                *self.pos.get_mut(&self.set[remove_index]).unwrap() = remove_index;
            }
            true
        } else {
            false
        }
    }
    
    fn get_random(&self) -> i32 {
        let index = rand::thread_rng().gen_range(0..self.set.len());
        self.set[index]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
