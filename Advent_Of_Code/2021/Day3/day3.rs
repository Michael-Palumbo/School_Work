use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

use std::collections::HashMap;

fn main() {
    let lines = open_and_parse_lines("input.txt");
    
    part1(lines.clone());

    part2(lines.clone());

}

fn part1(lines: Vec<String>) {
    let line_length = lines[0].len();

    let mut gamma = String::from("");
    let mut epsilon = String::from("");

    for index in 0..line_length{
        let column: Vec<char> = get_column(&lines, index);
        // println!("Column: {:?}", column);

        let c = mode(column);
        gamma.push(c);
        epsilon.push(if c == '0' {'1'} else {'0'});
    }

    let gamma = format_and_print_results("gamma", gamma);
    let epsilon = format_and_print_results("epsilon", epsilon);

    println!("Part 1 Result: Gamma*Epsilon= {}", gamma*epsilon);
}

fn get_column(lines: &Vec<String>, index: usize) -> Vec<char>{
    lines.iter()
          .map(|x| x.chars().nth(index).unwrap())
          .collect()
}

fn mode(group: Vec<char>) -> char {
    let mut occurrences = HashMap::new();
    for value in group {
        *occurrences.entry(value).or_insert(0) += 1;
    }

    //I'm not proud of this
    if occurrences.get(&'0') == occurrences.get(&'1') {
        return '1'
    }

    occurrences.into_iter()
               .max_by_key(|&(_,count)| count)
               .map(|(val, _)| val)
               .expect("Cannot compute the mode of zero numbers")
}

fn part2(lines: Vec<String>) {
    let line_length = lines[0].len();

    let mut gamma = lines.clone();
    let mut epsilon = lines.clone();

    // println!("Gamma Part");
    for index in 0..line_length{
        let gamma_col: Vec<char> = get_column(&gamma, index);
        let c = mode(gamma_col);
        gamma = filter_out(gamma, index, c, true);
        if gamma.len() == 1 {
            break;
        }
    }

    // println!("Epsilon Part");
    for index in 0..line_length{
        let epsilon_col: Vec<char> = get_column(&epsilon, index);
        let c = mode(epsilon_col);

        epsilon = filter_out(epsilon, index, c, false);
        if epsilon.len() == 1 {
            break;
        }
    }

    let gamma = gamma.pop().unwrap();
    let epsilon = epsilon.pop().unwrap();

    let gamma = format_and_print_results("gamma", gamma);
    let epsilon = format_and_print_results("epsilon", epsilon);

    println!("Part 2 Result: Gamma*Epsilon= {}", gamma*epsilon);
}

fn filter_out(lines: Vec<String> , index : usize,c : char, keep : bool) -> Vec<String> {
    lines.into_iter()
         .filter(|x| { 
            if keep {
                x.chars().nth(index).unwrap() == c 
            } else {
                x.chars().nth(index).unwrap() != c 
            }
         })
         .collect()
}

fn format_and_print_results(title: &str, gamma: String) -> isize{
    println!("{} binary: {:?}",title,gamma);
    let result = isize::from_str_radix(&gamma,2).unwrap_or_else(|_| panic!("Could not convert {} into val", title));
    println!("{} converted to: {}",title,result);
    result
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()

}