use std::collections::{BTreeMap,HashSet};
use std::collections::btree_map::Entry;
use std::ops::Bound;
#[derive(Debug,PartialEq,Eq,PartialOrd,Ord)]
struct Robot {
    pos: i32,
    health: i32,
    index: usize,
    is_right: bool, 
}
impl Robot {
    pub fn crash_time(&self, other: &Robot) -> Option<u32> {
        if (self.pos < other.pos && self.is_right && !other.is_right) || (self.pos > other.pos && !self.is_right && other.is_right) {
            let dist = (self.pos - other.pos).abs() as u32;
            //println!("{self:?} {other:?}");
            Some(dist / 2 + dist % 2)
        } else {
            None
        }

    }
    pub fn maybe_add_crash(&self, other: &Robot, crashes: &mut BTreeMap<u32, HashSet<(i32,i32)>>) {
        if let Some(crash_time) = self.crash_time(other) {
            let crash =  if self.pos <= other.pos {(self.pos, other.pos)} else {(other.pos, self.pos)};
            crashes.entry(crash_time).or_insert(HashSet::new()).insert(crash);
        }
    }
}
impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, healths: Vec<i32>, directions: String) -> Vec<i32> {
        let mut robots = Vec::new();
        let directions : Vec<char> = directions.chars().collect();
        for i in 0..positions.len() {
            let r = Robot {pos: positions[i], health: healths[i], index: i, is_right: directions[i] == 'R'};
            robots.push(r);
        }
        let mut crashes = BTreeMap::new();
        robots.sort();
        //println!("{:?}", robots);
        for r in robots.windows(2) {
            //println!("{:?}", r);
            r[0].maybe_add_crash(&r[1], &mut crashes);
        }
        let mut robots : BTreeMap<i32,Robot> = robots.into_iter().map(|r| (r.pos, r)).collect();
        //return Vec::new();
        //println!("{crashes:?}");
        while let Some((_, now_crashes)) = crashes.pop_first() {
            let mut kill = Vec::new();
            let mut dmg = Vec::new();
            let mut mid_check = Vec::new();
            for (r1p, r2p) in now_crashes {
                let r1h = robots.get(&r1p).unwrap().health;
                let r2h = robots.get(&r2p).unwrap().health;
                if r1h == r2h {
                    kill.push(r1p);
                    kill.push(r2p);
                    mid_check.push(r1p);
                } else if r1h < r2h {
                    kill.push(r1p);
                    if r2h > 1 {
                        dmg.push(r2p);
                    } else {
                        kill.push(r2p);
                        mid_check.push(r1p);
                    }
                } else {
                    if r1h > 1 {
                        dmg.push(r1p);
                    } else {
                        kill.push(r1p);
                        mid_check.push(r1p);
                    }
                    kill.push(r2p);
                }
            }
            for rp in kill {
                robots.remove(&rp);
            }
            for rp in dmg {
                robots.entry(rp).and_modify(|r| r.health -= 1);
                let r = robots.get(&rp).unwrap();
                if let Some((_, next_robot)) = if r.is_right { robots.range(r.pos+1..).next()} else {robots.range(..r.pos).last()} {
                    //println!("!{next_robot:?}");
                    r.maybe_add_crash(next_robot, &mut crashes);
                }
            }
            for p in mid_check {
                if let Some((_, rr)) = robots.range(p..).next() {
                    if let Some((_, rl)) = robots.range(..p).last() {
                        rl.maybe_add_crash(rr, &mut crashes);
                    }
                }
            }
            //println!("{crashes:?}");
        }
        /*

            let mut next_health = None;
            let mut it = robots.iter_mut().peekable();
            while let Some(ref mut robot) = it.next() {
                if let Some(health) = next_health {
                    robot.health = health;
                    next_health = None;
                } else if let Some(next_robot) = it.peek() {
                    if robot.is_right && !next_robot.is_right && min_dist == next_robot.pos - robot.pos {
                        if robot.health == next_robot.health {
                            robot.health = 0;
                            next_health = Some(0);
                        } else if robot.health > next_robot.health {
                            robot.health -= 1;
                            next_health = Some(0);
                        } else {
                            robot.health = 0;
                            next_health = Some(next_robot.health - 1);
                        }
                    }
                } else {
                    break;
                }
            }
            robots = robots.iter().filter_map(|r|
                if r.health <= 0 {
                    None
                } else {
                    Some(
                        Robot {
                            pos: r.pos + ((min_dist/2 + min_dist % 2) * (if r.is_right {1} else {-1})),
                            ..*r
                        }
                    )
                }
            ).collect();
        }

        let mut robots : Vec<(usize, i32)> = robots.iter().map(|r| (r.index, r.health)).collect();
        robots.sort();
        */
        let mut robots : Vec<(usize, i32)> = robots.values().map(|r| (r.index, r.health)).collect();
        robots.sort();
        robots.iter().map(|(_, h)| *h).collect()
    }
}
