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
use std::collections::HashSet;
impl Solution {
    fn _del_nodes(root: &Rc<RefCell<TreeNode>>, to_delete: &mut HashSet<i32>) -> (bool, Vec<Option<Rc<RefCell<TreeNode>>>>) {
        let mut forest = Vec::new();
        let mut root = root.borrow_mut();
        let del = to_delete.remove(&root.val);
        if let Some(left) = &root.left {
            let (left_del, mut left_forest) = Self::_del_nodes(&left, to_delete);
            if left_del {
                root.left = None;
            } else if del {
                forest.push(Some(left.clone()));
            }
            forest.append(&mut left_forest);
        }
        if let Some(right) = &root.right {
            let (right_del, mut right_forest) = Self::_del_nodes(&right, to_delete);
            if right_del {
                root.right = None;
            } else if del {
                forest.push(Some(right.clone()));
            }
            forest.append(&mut right_forest);
        }
        (del, forest)
    }
    pub fn del_nodes(root: Option<Rc<RefCell<TreeNode>>>, to_delete: Vec<i32>) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if let Some(root) = &root {
            let mut to_delete = HashSet::from_iter(to_delete.into_iter());
            let (del_root, mut forest) = Self::_del_nodes(&root, &mut to_delete);
            if !del_root {
                forest.push(Some(root.clone()));
            }
            forest
        } else {
            Vec::new()
        }
    }
}
