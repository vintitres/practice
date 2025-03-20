impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut group_id: Vec<usize> = (0..n).collect();
        let mut group_weight = vec![i32::MAX; n];
        let mut group_content: Vec<Vec<usize>> = (0..n).map(|node| vec![node]).collect();
        for edge in edges {
            let u = *edge.get(0).unwrap() as usize;
            let v = *edge.get(1).unwrap() as usize;
            let w = edge.get(2).unwrap();
            let mut group1 = *group_id.get(u).unwrap();
            let mut group2 = *group_id.get(v).unwrap();
            if group1 != group2 {
                let g1len = group_content.get(group1).unwrap().len();
                let g2len = group_content.get(group2).unwrap().len();
                if g1len < g2len {
                    std::mem::swap(&mut group1, &mut group2);
                }
                let g2 = group_content.get(group2).unwrap().clone();
                for node in &g2 {
                    group_id[*node] = group1;
                }
                group_content.get_mut(group1).unwrap().extend(g2);
                let g2w = *group_weight.get(group2).unwrap();
                group_weight[group1] &= g2w;

            }
            group_weight[group1] &= w;
        }

        query.iter().map(|q| {
            let s = *q.get(0).unwrap() as usize;
            let t = *q.get(1).unwrap() as usize;
            let mut group1 = *group_id.get(s).unwrap();
            let mut group2 = *group_id.get(t).unwrap();
            if group1 != group2 {
                -1
            } else {
                group_weight[group1]
            }
        }
        
        ).collect()
    }
}
