// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut next = head.unwrap().next;
        let mut sum = 0;
        let mut root : Option<Box<ListNode>> = None;
        let mut current = &mut root;
        while let Some(cur) = next {
            if cur.val == 0 {
                *current = Some(Box::new(ListNode::new(sum)));
                current = &mut current.as_mut().unwrap().next;
                sum = 0;
            } else {
                sum += cur.val;
            }
            next = cur.next;
        }
        root
    }
}
