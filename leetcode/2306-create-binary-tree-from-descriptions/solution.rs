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
use std::collections::{HashMap,HashSet};
impl Solution {
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes : HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        for desc in descriptions {
            let parent = desc[0];
            let child = desc[1];
            let child_id = child;
            let is_left = desc[2] == 1;
            let child = Rc::clone(&nodes.entry(child).or_insert(Rc::new(RefCell::new(TreeNode::new(child)))));
            let mut parent = nodes.entry(parent).or_insert(Rc::new(RefCell::new(TreeNode::new(parent))));
            if is_left {
                parent.borrow_mut().left = Some(child);
            } else {
                parent.borrow_mut().right = Some(child);
            }
        }
        let mut all : HashSet<i32> = nodes.values().map(|n| n.borrow().val).collect();
        for node in nodes.values() {
            if let Some(c) = &node.borrow().left {
                all.remove(&c.borrow().val);
            }
            if let Some(c) = &node.borrow().right {
                all.remove(&c.borrow().val);
            }
        }
        let root_id = all.iter().next().unwrap();
        Some(nodes.get(root_id).unwrap().clone())
    }
}
