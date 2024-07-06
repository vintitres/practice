use std::collections::HashSet;
#[derive(Clone,Debug)]
struct Group {
    index: usize,
    set: HashSet<usize>,
}
impl Group {
    pub fn len(&self, groups: &Vec<Group>) -> usize {
        if self.set.is_empty() {
            groups[self.index].len(&groups)
        } else {
            self.set.len()
        }
    }
    pub fn connected(&self, other: usize, groups: &Vec<Group>) -> bool {
        if self.set.is_empty() {
            groups[self.index].connected(other, &groups)
        }else {
            self.set.contains(&other)
        }
    }
    pub fn add(&mut self, elems: &HashSet<usize>) {
        if self.set.is_empty() {
            panic!("add to bad");
        }
        for &e in elems {
            self.set.insert(e);
        }
    }
    pub fn join(u: usize, v: usize, groups: &mut Vec<Group>) {
        let (u, v) = if groups[u].len(&groups) > groups[v].len(&groups) {
            (v, u)
        } else {
            (u, v)
        };
        let u = groups[u].index;
        let v = groups[v].index;

        //println!("{} {} {:?} {:?}", u, v, groups[u], groups[v]);
        let uset = groups[u].set.clone();
        groups[v].add(&uset);
        for i in uset {
            groups[i] = Group {
                set: HashSet::new(),
                index: v,
            };
        }
    }
}
impl Solution {
    pub fn max_num_edges_to_remove(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut groups = Vec::new();
        let mut both_groups = Vec::new();
        for i in 0..n {
            groups.push(Group{ set: HashSet::from([i]), index: i});
        }
        let mut edges : Vec<(i32, usize, usize)> = edges.iter().map(|e| (-e[0], (e[1] - 1) as usize, (e[2] - 1) as usize)).collect();
        edges.push((-1, 0, 0));
        edges.push((-2, 0, 0));
        edges.sort();
        let mut removable = 0;
        let mut last_key = -3;
        for (key, u, v) in edges {
            if key != last_key {
                match -key {
                    1 => {
                        if groups[0].len(&groups) != n {
                            return -1;
                        }
                        groups = both_groups.clone();
                    },
                    2 => {
                        both_groups = groups.clone();
                    },
                    3 => (),
                    _ => unimplemented!(),
                };
                last_key = key;
            }
            if groups[u].connected(v, &groups) {
                removable += 1;
            } else {
                Group::join(u, v, &mut groups);
            }
        }
        if groups[0].len(&groups) != n {
            return -1;
        }
        removable - 2
    }
}
