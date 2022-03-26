use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

fn main(){
    let lines = open_and_parse_lines("input.txt");

    let mut sum = 0;

    // bins denotes [')', ']', '}', '>']

    let mut passed_lines: Vec<String> = Vec::new();

    for line in &lines {
        let is_valid = check_line(&line);
        match is_valid {
            Brace::INVALID(')') => sum += 3,
            Brace::INVALID(']') => sum += 57,
            Brace::INVALID('}') => sum += 1197,
            Brace::INVALID('>') => sum += 25137,
            _ => passed_lines.push(line.clone()),
        }
        // println!("Result : {:?}", is_valid );
    }

    println!("Task 1 Sum: {}", sum);

    let mut sums: Vec<usize> = Vec::new();

    for line in &passed_lines {
        let mut task_2_sum = 0;
        let remaining_chars = finish_lines(&line);
        // println!("Stack: {:?}", remaining_chars);
        for c in remaining_chars.iter().rev() {
            task_2_sum *= 5;
            match c {
                '(' => task_2_sum += 1,
                '[' => task_2_sum += 2,
                '{' => task_2_sum += 3,
                '<' => task_2_sum += 4,
                _ => panic!("PATTERN ERROR"),
            }
            // println!("Sum: {}", task_2_sum);
        }
        sums.push(task_2_sum);
    }

    // println!("Array:\n{:?}", sums);

    sums.sort();

    let middle = sums.get( sums.len()/2 ).unwrap();

    println!("Task 2 Sum: {}", middle);

}

fn check_line(line: &String) -> Brace {
    let mut stack : Vec<char> = Vec::new();
    for c in line.chars(){     
        if "([{<".contains(c) {
            stack.push(c)
        } else if ")}]>".contains(c) {
            let temp = stack.pop().unwrap();
            if !check_match(&temp, &c) {
                return Brace::INVALID(c);
            }
        }
    }
    Brace::VALID
}

fn finish_lines(line: &String) -> Vec<char> {
    let mut stack : Vec<char> = Vec::new();

    // Set up stack
    for c in line.chars(){     
        if "([{<".contains(c) {
            stack.push(c)
        } else if ")}]>".contains(c) {
            let temp = stack.pop().unwrap();
            if !check_match(&temp, &c) {
                panic!("SHOULD NOT HAVE REACHED HERE")
            }
        }
    }
    stack
}

fn check_match(popped_char: &char, c: &char) -> bool{
    match popped_char {
        '(' => *c == ')',
        '[' => *c == ']',
        '{' => *c == '}',
        '<' => *c == '>',
        _ => panic!("ERROR OCCURED IN CHECK_MATCH"),
    }
}


fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}

#[derive(Debug)]
enum Brace {
    INVALID(char),
    VALID,
}