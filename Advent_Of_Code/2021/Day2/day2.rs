use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

fn main() {

    let mut ver_pos : i64 = 0;
    let mut hor_pos : i64 = 0;
    let mut aim : i64 = 0;

    let lines = open_and_parse_lines("input.txt");

    for instruction in lines.iter() {
        let mut seperate_iter = instruction.split(' ');
        let command = seperate_iter.next().unwrap();
        let unit : i64 = seperate_iter.next().unwrap().parse().expect("Could not parse unit");
        match command {
            "forward" => {hor_pos += unit; ver_pos += aim * unit}, 
            "down" => aim += unit, 
            "up" => aim -= unit, 
            _ => println!("Command not found! {}", command),
        }
    }

    println!("X: {} + Y: {} = {}", hor_pos, ver_pos, ver_pos*hor_pos);

}

// match command {
//     "forward" => hor_pos += unit, 
//     "down" => ver_pos += unit, 
//     "up" => ver_pos -= unit, 
//     _ => println!("Command not found! {}", command),
// }

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()

}
