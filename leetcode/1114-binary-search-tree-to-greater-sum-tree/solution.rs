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
    fn bst_to_gst_with_sum(root: &Option<Rc<RefCell<TreeNode>>>, extra: i32) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut root = root.as_ref().unwrap().borrow_mut();
        root.val += extra + Self::bst_to_gst_with_sum(&root.right, extra);
        Self::bst_to_gst_with_sum(&root.left, root.val) + root.val - extra
    }
    pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::bst_to_gst_with_sum(&root, 0);
        root
    }
}
