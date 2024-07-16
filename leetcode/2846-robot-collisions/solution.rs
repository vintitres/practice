use std::collections::{BTreeMap,HashSet};
use std::collections::btree_map::Entry;
use std::cmp::Ordering;
#[derive(Debug,PartialEq,Eq,PartialOrd,Ord)]
enum Direction {
    Left,
    Right,
}
#[derive(Debug,PartialEq,Eq,PartialOrd,Ord)]
struct Robot {
    pos: i32,
    health: i32,
    index: usize,
    direction: Direction, 
}
impl Robot {
    pub fn is_alive(&self) -> bool {
        self.health > 0
    }
    pub fn kill(&mut self) {
        self.health = 0;
    }
    pub fn hit(&mut self) {
        self.health -= 1;
    }
}
impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, healths: Vec<i32>, directions: String) -> Vec<i32> {
        let mut robots : Vec<Robot> = positions.iter().zip(healths.iter()).zip(directions.chars()).enumerate().map(|(index, ((&pos, &health), direction))| Robot{
            pos, index, health,
            direction: if direction == 'R' {
                Direction::Right
            } else {
                Direction::Left
            }
        }).collect();
        robots.sort();
        let mut stack = Vec::new();
        let mut surv = Vec::new();
        for mut cur in robots.into_iter() {
            match cur.direction {
                Direction::Right => stack.push(cur),
                Direction::Left => {
                    while let Some(mut prev) = stack.pop() {
                        match prev.health.cmp(&cur.health) {
                            Ordering::Equal => {
                                prev.kill();
                                cur.kill();
                            },
                            Ordering::Greater => {
                                prev.hit();
                                cur.kill();
                            },
                            Ordering::Less => {
                                prev.kill();
                                cur.hit();
                            }
                        }
                        if prev.is_alive() {
                            stack.push(prev);
                        }
                        if !cur.is_alive() {
                            break;
                        }
                    }
                    if cur.is_alive() {
                        surv.push(cur);
                    }
                },
            }
        }
        
        
        let mut robots : Vec<(usize, i32)> = stack.iter().chain(surv.iter()).map(|r| (r.index, r.health)).collect();
        robots.sort();
        robots.iter().map(|(_, h)| *h).collect()
    }
}
