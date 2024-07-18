// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    fn pairs_and_depths(root: &Option<Rc<RefCell<TreeNode>>>, distance: usize) -> (i32, Vec<i32>) {
        let mut pairs : i32 = 0;
        let mut depths = Vec::new();
        if let Some(root) = &root {
            let left = &root.borrow().left;
            let right = &root.borrow().right;
            if left.is_none() && right.is_none() {
                depths.push(1);
            } else {
                let (left_pairs, left_depths) = Self::pairs_and_depths(left, distance);
                let (right_pairs, right_depths) = Self::pairs_and_depths(right, distance);
                pairs += left_pairs + right_pairs;
                pairs += left_depths.iter().enumerate().map(|(depth, count)| {
                    let r = std::cmp::max(0, distance as i32 - depth as i32 - 1) as usize;
                    let right_leaves = right_depths.iter().take(r).sum::<i32>();
                    //println!("{depth} {r} {count}*{right_leaves}");
                    count * right_leaves
                }).sum::<i32>();
                depths.push(0);
                for i in 0..std::cmp::max(left_depths.len(), right_depths.len()) {
                    depths.push(left_depths.get(i).unwrap_or(&0) + right_depths.get(i).unwrap_or(&0));
                }
            }
        }
        //println!("{:?} {} {:?}", root, pairs, depths);
        (pairs, depths)
    }
    pub fn count_pairs(root: Option<Rc<RefCell<TreeNode>>>, distance: i32) -> i32 {
        Self::pairs_and_depths(&root, distance as usize).0
    }
}
