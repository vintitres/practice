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
impl ListNode {
    pub fn iter(self) -> ListNodeIterator {
        ListNodeIterator::new(Some(Box::new(self)))
    }
}
struct ListNodeIterator {
    current: Option<Box<ListNode>>,
}
impl ListNodeIterator {
    pub fn new(node: Option<Box<ListNode>>) -> Self {
        Self {
            current: node
        }
    }
}
impl Iterator for ListNodeIterator {
    type Item = i32;
    fn next(&mut self) -> Option<Self::Item> {
        let mut val = None;
        if let Some(node) = self.current.take() {
            val = Some(node.val);
            self.current = node.next;
        } else {
            return None;
        }
        val
    }
}
impl Solution {
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut v : Vec<i32> = Vec::from_iter(head.unwrap().iter());
        let poss : Vec<usize> = v.windows(3).enumerate().map(|(i, window)| if (window[0] < window[1] && window[2] < window[1]) || (window[0] > window[1] && window[2] > window[1]) {Some(i + 1)} else {None}).flatten().collect();
        if poss.len() < 2 {
            vec![-1, -1]
        } else {
            vec![
                poss.windows(2).map(|w| w[1] - w[0]).min().unwrap() as i32,
                (poss.last().unwrap() - poss.first().unwrap()) as i32 
            ]
        }
        
    }
}
