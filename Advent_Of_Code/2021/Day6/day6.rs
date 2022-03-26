use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

const MAX_DAYS: usize = 9; // 0 to 8 inclusive

fn main(){
    let lines = open_and_parse_lines("input.txt");
    let initial_fishes: Vec<usize> = lines.iter().
            flat_map(|line| 
                line.split(',')
                .map(|x| x.parse().unwrap())
            ).collect();
    
    //     let initial_fishes: Vec<usize> = lines.get(0).unwrap().split(',').map(|x| x.parse().unwrap()).collect();

    let mut days = [0; MAX_DAYS];

    //load initial fish
    for fish in initial_fishes {
        days[fish] += 1;
    }

    println!("Fishes      : {:?}", days);

    run_simulation(&mut days, 256);

    let sum : usize = days.iter().sum();

    println!("Part 1: {}", sum);

}

fn run_simulation(days: &mut [usize; MAX_DAYS], iterations: usize ){
    let mut carry_over = 0;
    for _generation in 0..iterations {
        for index in (0..days.len()).rev() {
            if index == 8 {
                carry_over = days[index];
                days[index] = 0;
            } else if index == 0 {
                days[6] += days[index];
                days[8] = days[index];
                days[index] = carry_over;
            } else {
                let temp = days[index];
                days[index] = carry_over;
                carry_over = temp;
            }
        }
        // println!("generation: {} {:?}", _generation,days);
    }
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}