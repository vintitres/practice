impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let mut opens_stack = Vec::new();
        let mut text = String::new();
        for c in s.chars() {
            if c == '(' {
                opens_stack.push(text);
                text = String::new();
            } else if c == ')' {
                text = text.chars().rev().collect();
                text = opens_stack.pop().unwrap() + &text;

            } else {
                text.push(c);
            }
        }
        text
    }
}
