use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

fn main(){
    let lines = open_and_parse_lines("input.txt");
    let crabs: Vec<isize> = lines.iter().
            flat_map(|line| 
                line.split(',')
                .map(|x| x.parse().unwrap())
            ).collect();

    let max_val = crabs.iter().max().unwrap();
        
    let linear_fuel_burn = | x :&isize, p:&isize | { (x-p).abs() };

    let exponential_fuel_burn = | x :&isize, p:&isize | { (x-p).abs()*((x-p).abs() + 1)/2 };

    let task_1 : isize = (0..*max_val).map(
        |x| {
            crabs.iter().map(|crab| exponential_fuel_burn(&x,&crab)).sum()
        } ).min().unwrap();

    println!("Task {:?}", task_1);
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}