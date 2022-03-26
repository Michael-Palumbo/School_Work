use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

fn main(){
    let lines = open_and_parse_file("input.txt");

    let mut octupus_grid: Vec<Vec<usize>> = lines.iter()
                            .map(
                                |x| x.chars().map(
                                    |y| y.to_digit(10).unwrap() as usize
                                    ).collect() 
                                ).collect();

    println!("Octupus_grid {:?}",octupus_grid);

    let mut flashes = 0;

    let mut step = 0;
    while !check_sychronized(&octupus_grid) {
        flashes += calculate_energy(&mut octupus_grid);
        step += 1;
        // println!("\nAfter step {}:",i);
        // print_grid(&octupus_grid);
        // println!("Gridv2\n{:?}", octupus_grid);
    }
    println!("Steps: {}", step);
    println!("Flashes : {}", flashes);

}

// fn print_grid(grid: &Vec<Vec<usize>>) {
//     grid.iter().for_each(|line| println!("{:?}", line));
// }

fn calculate_energy(grid : &mut Vec<Vec<usize>>) -> usize{
    for row in 0..grid.len() {
        for col in 0..grid[0].len() {
            grid[row][col] += 1; 
        }
    }

    let mut flash_count = 0;

    for row in 0..grid.len() {
        for col in 0..grid[0].len() {
            if grid[row][col] > 9 {
                flash_count += flash_energy(grid, row, col);
            }
        }
    }
    flash_count
}

const NEIGHBORS: [(isize,isize); 8] = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)];

fn flash_energy(grid: &mut Vec<Vec<usize>>, row: usize, col: usize) -> usize{
    let mut flash_count = 1;
    grid[row][col] = 0;
    for (offset_r, offset_c) in NEIGHBORS {
        let o_row = (row as isize) + offset_r;
        let o_col = (col as isize) + offset_c;
        // Check if its inbounds
        if  check_inbounds(o_row, o_col, grid.len(), grid[0].len()) {
            if grid[o_row as usize][o_col as usize] != 0 {
                grid[o_row as usize][o_col as usize] += 1;
                if grid[o_row as usize][o_col as usize] > 9 {
                    flash_count += flash_energy(grid, o_row as usize, o_col as usize);
                }
            }
        }
    }
    flash_count
}

fn check_inbounds(o_row: isize, o_col: isize, height: usize, width: usize) -> bool {
    o_row >= 0 && o_col >= 0 && 
    (o_row as usize) < height && 
    (o_col as usize) < width
}

fn check_sychronized(grid: &Vec<Vec<usize>>) -> bool {
    for row in 0..grid.len() {
        for col in 0..grid[0].len() {
            if grid[row][col] != 0 {
                return false;
            }
        }
    }
    true
}

fn open_and_parse_file(filename: &str) -> Vec<String>{
    let file = File::open(filename).expect("Couldn't open file");
    BufReader::new(file).lines().map(|line| line.unwrap()).collect()
}