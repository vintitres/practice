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
        let mut f = |child_ref: &mut Option<Rc<RefCell<TreeNode>>>| {
            if let Some(child) = &child_ref {
                let (child_del, mut child_forest) = Self::_del_nodes(&child, to_delete);
                forest.append(&mut child_forest);
                if child_del {
                    *child_ref = None;
                } else if del {
                    forest.push(Some(child.clone()));
                }
            }
        };
        f(&mut root.left);
        f(&mut root.right);
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
