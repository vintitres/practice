use std::collections::HashMap;
use std::iter::Peekable;
struct FormulaNums(HashMap<String, u64>);
impl FormulaNums {
    pub fn add(&mut self, atom: &String, count: u64) {
        *self.0.entry(atom.to_string()).or_insert(0) += count;
    } 
    pub fn mul(&mut self, x: u64) {
        for atom_count in self.0.values_mut() {
            *atom_count *= x;
        }
    } 
    pub fn expand(&mut self, atoms: &FormulaNums) {
        for (atom, &count) in atoms.0.iter() {
            self.add(atom, count);
        }
    }
    pub fn new() -> Self {
        Self(HashMap::new())
    }
    pub fn desc(&self) -> String {
        let mut atoms : Vec<(String, u64)> = self.0.iter().map(|(a, &c)| (a.clone(), c)).collect();
        atoms.sort();
        atoms.iter().map(|(a, c)| if *c == 1 {a.clone()} else {a.clone() + &c.to_string()}).collect()
    }
}

impl Solution {
    fn read_num(it: &mut Peekable<impl Iterator<Item=char>>) -> u64 {
        let mut num = 0;
        while let Some(c) = it.next_if(|c| c.is_digit(10)) {
            num *= 10;
            num += c as u64 - '0' as u64;
        }
        if num > 0 { num } else {1}
    }
    fn read_atom(it: &mut Peekable<impl Iterator<Item=char>>) -> String {
        let mut atom = String::from(it.next().unwrap());
        while let Some(c) = it.next_if(|c| c.is_lowercase()) {
            atom.push(c);
        }
        atom
    }
    pub fn count_of_atoms(formula: String) -> String {
        let mut atoms_stack = Vec::new();
        let mut atoms = FormulaNums::new();
        let mut it = formula.chars().peekable();
        while let Some(&c) = it.peek() {
            if c == '(' {
                it.next();
                atoms_stack.push(atoms);
                atoms = FormulaNums::new();
            } else if c == ')' {
                it.next();
                atoms.mul(Self::read_num(&mut it));
                let mut new_atoms = atoms_stack.pop().unwrap();
                new_atoms.expand(&atoms);
                atoms = new_atoms;
            } else {
                let atom = Self::read_atom(&mut it);
                let count = Self::read_num(&mut it);
                atoms.add(&atom, count);
            }
        }
        atoms.desc()
    }
}
