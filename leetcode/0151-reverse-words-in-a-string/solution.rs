impl Solution {
    pub fn reverse_words(s: String) -> String {
         s.split(" ").filter(|&w|w != "").collect::<Vec<&str>>().into_iter().rev().fold(String::new(), |s, w| if s == ""  {w.to_string()} else {s + " " + w})
    }
}
