use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

use std::fmt;

// const BOARD_SIZE = 5;

fn main(){
    let lines = open_and_parse_lines("input.txt");

    let input:Vec<usize> = lines.get(0).unwrap().split(',').map(|x| x.parse().unwrap()).collect(); // First Line is the input

    println!("Input: {:?}", input);

    let mut boards = make_boards(lines);

    // 'outer : for number in input {    
    //     // println!("Marking {}",number);
    //     for board in boards.iter_mut() {
    //         board.mark(number);
    //         if board.check_win() {
    //             println!("Board Won!\n{}",board);
    //             println!("Number won on {}", number);
    //             println!("Unmarked sum is {}", board.sun_unmarked());
    //             println!("Result {}", board.sun_unmarked()*number);
    //             break 'outer
    //         }
    //         // println!("{}",board);
    //     }
    // }

    'outer : for number in input {    
        // println!("Marking {}",number);
        for index in (0..boards.len()).rev() {
            let length = boards.len();
            let board: &mut Board = boards.get_mut(index).unwrap();
            board.mark(number);
            if board.check_win() {
                if length == 1{
                    println!("Number won on {}", number);
                    println!("Unmarked sum is {}", board.sun_unmarked());
                    println!("Result {}", board.sun_unmarked()*number);                
                    break 'outer
                } else {
                    boards.remove(index);
                }
            }
            
            // println!("{}",board);
        }
    }

    // for (index, bingo) in boards.iter().enumerate() {
    //     println!("{}:\n{}",index,bingo);
    // }
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}

fn make_boards(lines : Vec<String>) -> Vec<Board>{
    let mut line_iter = lines.iter();
    line_iter.next();
    line_iter.next();

    let mut bingo_boards : Vec<Board> = Vec::new();
    let mut board: Board = Board{bingo_board: Vec::new()};
    for line in line_iter {
        //println!("Parsing Line {}", line);
        if line == "" {
            //println!("Reached New Line");
            bingo_boards.push(board);
            board = Board{bingo_board: Vec::new()};
        } else {
            let parsed_line: Vec<MarkVal> = line.trim().split_whitespace()
                    .map(|x| {
                        //println!("Value Parsing: ${}$", x);
                        MarkVal::new(x.parse().unwrap())
                    })
                    .collect();
            board.bingo_board.push(parsed_line);
        }
    }
    // If there is still room for a board
    if board.bingo_board.len() != 0 {
        bingo_boards.push(board);
    }

    // for (index, bingo) in bingo_boards.iter().enumerate() {
    //     println!("{}:\n{}",index,bingo);
    // }

    bingo_boards
}

#[derive(Debug)]
struct MarkVal {
    val: usize,
    marked: bool,
}

impl MarkVal{
    pub fn new(value : usize) -> Self{
        Self {val: value, marked : false }
    }
}

impl fmt::Display for MarkVal {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        if self.marked {
            write!(f, "*{}", self.val)
        }else{
            write!(f, "{}", self.val)
        }
    }
}

#[derive(Debug)]
struct Board {
    bingo_board: Vec<Vec<MarkVal>>,
}

impl Board {
    fn mark(&mut self, value: usize){
        for row in self.bingo_board.iter_mut(){
            for col in row{
                if col.val == value {
                    col.marked = true;
                }
            }
        }
    }
    fn check_win(&self) -> bool{
        for row in self.bingo_board.iter() {
            if row.iter().filter(|x| x.marked).count() == row.len() {
                return true;
            }
        }

        for index in 0..self.bingo_board.get(0).unwrap().len() {
            if self.bingo_board.iter()
                               .map(|x| x.get(index).unwrap())
                               .filter(|x| x.marked).count() == self.bingo_board.get(0).unwrap().len() {
                return true;
            }
        }

        false
    }
    fn sun_unmarked(&self) -> usize {
        let mut count = 0;
        for row in self.bingo_board.iter(){
            for col in row{
                if !col.marked {
                    count += col.val;
                }
            }
        }
        count
    }
}

impl fmt::Display for Board {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut result = String::new();
        for row in &self.bingo_board{
            for col in row{
                let temp = format!("{} ",col);
                result.push_str(&temp);
            }
            result.push_str(&"\n");
        }
        write!(f, "{}", result)
    }
}