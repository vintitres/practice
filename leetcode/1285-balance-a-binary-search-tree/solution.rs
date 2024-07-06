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
    fn traverse(root: &Option<Rc<RefCell<TreeNode>>>, mut list: &mut Vec<i32>) {
        if root.is_none() {
            return;
        }
        let mut root = root.as_ref().unwrap().borrow_mut();
        Self::traverse(&root.left, &mut list);
        list.push(root.val);
        Self::traverse(&root.right, &mut list);
    } 
    fn build_bst(vals: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        if vals.len() == 0 {
            return None;
        }
        let mid = vals.len() / 2;
        Some(Rc::new(RefCell::new(TreeNode { val: vals[mid], left: Self::build_bst(&vals[..mid]), right: Self::build_bst(&vals[mid + 1..]) })))

    }
    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut list = Vec::<i32>::new();
        Self::traverse(&root, &mut list);
        Self::build_bst(&list)
    }
}
