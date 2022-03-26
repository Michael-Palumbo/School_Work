use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

fn main() {
    
    let v = openAndParseLines("input.txt");

    let mut count = 0;

    // Part 1
    for index in 0..v.len()-1{
        if &v[index] < &v[index+1]{
            count+=1;
        }
    }

    println!("Part 1 Length {}", count);   

    count = 0;

    // Part 2
    for index in 0..v.len()-3{
        if &v[index]+&v[index+1]+&v[index+2] < &v[index+1]+&v[index+2]+&v[index+3] {
            count+=1;
        }
    }
    println!("Part 2 Length {}", count);   
}



fn openAndParseLines(filename: &str) -> Vec<i32> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    let mut v : Vec<i32> = Vec::new();

    for line in reader.lines() {
        let unwrapped_line = line.unwrap();
        let num_line : i32 = unwrapped_line.parse().expect("Line couldn't be parsed");
        v.push(num_line);
    }
    return v;
}
