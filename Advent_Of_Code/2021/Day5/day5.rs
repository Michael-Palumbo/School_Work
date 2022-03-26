use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

use std::cmp::Ordering;

const SIZE : usize = 10;

fn main(){

    let input = open_and_parse_lines("input.txt");

    let mut board = vec![[0; SIZE]; SIZE];

    println!("PRINT A");

    let mut lines: Vec<Line> = Vec::new();

    for given_line in input {
        let two_points: Vec<&str> = given_line.split("->").map(|x| x.trim()).collect();
        let point_1: Vec<usize> = two_points.get(0).unwrap().split(",").map(|x| x.parse().unwrap()).collect();
        let point_2: Vec<usize> = two_points.get(1).unwrap().split(",").map(|x| x.parse().unwrap()).collect();
        lines.push( Line { 
            p1: Point {x: *point_1.get(0).unwrap(), y: *point_1.get(1).unwrap()},
            p2: Point {x: *point_2.get(0).unwrap(), y: *point_2.get(1).unwrap()}
            } );
        
    }

    println!("PRINT B");


    // for line in lines {
    //     println!("{:?}", line);
    // }

    for line in lines { 
        line.plot_points( &mut board);
    }

    println!("PRINT C");

    // println!("DEBUG {:?}", board);

    let mut display = String::from("");
    for row in &board {
        for col in row {
            match col.cmp(&1) {
                Ordering::Less => display.push_str("."),
                Ordering::Greater => display.push_str("2"),
                Ordering::Equal => display.push_str("1"),
            }
        }
        display.push_str("\n");
    }
    println!("{}",display);


    // -- THE BOARD COUNTING

    let mut count = 0;
    for row in &board {
        for col in row {
            if col > &1 {
                count += 1;
            }
        }
    }

    println!("Count {}", count);
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}

#[derive(Copy, Clone, Debug)]
struct Point {
    x : usize,
    y : usize,
}

#[derive(Copy, Clone, Debug)]
struct Line {
    p1 : Point,
    p2 : Point,
}

impl Line {
    fn plot_points(&self, board: &mut Vec<[usize; SIZE]>){

        if self.p1.x > SIZE-1 || self.p2.x > SIZE-1 || self.p1.y > SIZE-1 || self.p2.y > SIZE-1 {
            println!("LINE OVER 999 {:?}", self);
            return;
        }

        let (p1, p2) = if self.p1.x == self.p2.x {
            if self.p1.y < self.p2.y {
                (self.p1, self.p2)
            } else {
                (self.p2, self.p1)
            }
        }else {
            if self.p1.x < self.p2.x {
                (self.p1, self.p2)
            } else {
                (self.p2, self.p1)
            }
        };

        // println!("Line: {:?}", self);

        //println!("x1 {} y1 {} x2 {} y2 {} ",p1.x,p1.y,p2.x,p2.y);
        for x in p1.x..p2.x+1 {
            for y in p1.y..p2.y+1 {
                board[y][x] += 1;
            }
        }
    }
}