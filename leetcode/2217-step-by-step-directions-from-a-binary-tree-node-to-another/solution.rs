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
    fn find_path(root: &Option<Rc<RefCell<TreeNode>>>, value: i32) -> Option<String> {
        if let Some(root) = root {
            if root.borrow().val == value {
                return Some("".to_string())
            }
            if let Some(path) = Self::find_path(&root.borrow().left, value) {
                return Some("L".to_string() + &path);
            }
            if let Some(path) = Self::find_path(&root.borrow().right, value) {
                return Some("R".to_string() + &path);
            }
        }
        None
    }
        
    pub fn get_directions(root: Option<Rc<RefCell<TreeNode>>>, start_value: i32, dest_value: i32) -> String {
        let path_to_start = Self::find_path(&root, start_value).unwrap();
        let path_to_dest = Self::find_path(&root, dest_value).unwrap();
        let common_path_len = path_to_start.chars().zip(path_to_dest.chars()).take_while(|(s,d)| s == d).count();
        String::from_utf8(vec![b'U'; path_to_start.len() - common_path_len]).unwrap() + &path_to_dest[common_path_len..]
        
    }
}
