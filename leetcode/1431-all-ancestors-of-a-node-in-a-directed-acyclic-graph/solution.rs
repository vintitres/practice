use std::collections::BTreeSet;
impl Solution {
    fn anc(parents: &Vec<BTreeSet<i32>>, mut ancestors: &mut Vec<Option<BTreeSet<i32>>>, index: usize) -> BTreeSet<i32> {
        if ancestors[index].is_some() {
            ancestors[index].as_ref().unwrap().clone()
        } else {
            let mut ancestorsi = BTreeSet::new();
            ancestorsi.extend(parents[index].iter());
            for &parent in parents[index].iter() {
                ancestorsi.extend(Self::anc(&parents, &mut ancestors, parent as usize).iter());
            }
            ancestors[index] = ancestorsi.iter().map(|a| Some(*a)).collect();
            ancestorsi
        }
    }
    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut parents: Vec<BTreeSet<i32>> = vec![BTreeSet::new(); n as usize];
        for edge in edges {
            parents[edge[1] as usize].insert(edge[0]);
        }
        let mut ancestors: Vec<Option<BTreeSet<i32>>> = vec![None; n as usize];
        for i in 0..(n as usize) {
            Self::anc(&parents, &mut ancestors, i);
        }
        ancestors.iter().map(|opanc| opanc.as_ref().unwrap().iter().map(|&n| n).collect()).collect()
    }
}
