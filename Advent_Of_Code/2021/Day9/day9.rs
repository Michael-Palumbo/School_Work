use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File; 
use std::vec::Vec;

use std::convert::TryInto;

#[derive(Copy, Clone, Debug)]
struct Point {
    row:usize,
    col:usize
}

fn main() {
    let lines = open_and_parse_lines("input.txt");

    let grid: Vec<Vec<usize>> = lines.iter()
                    .map(
                        |x| x.chars().map(
                            |y| y.to_digit(10).unwrap() as usize
                            ).collect() 
                        ).collect();

    let mut low_points: Vec<Point> = Vec::new();

    for row in 0..grid.len() {
        for col in 0..grid[row].len() { 
            if check_neighbors(&grid, row, col) {
                low_points.push( Point{ row , col } );
            }
        }
    }

    let sum: usize = low_points.iter().map(|p| grid[p.row][p.col] + 1).sum();

    // println!("Low-Points {:?}", low_points);
    println!("Task 1 Sum {}", sum);

    // for low_point in low_points {
    //     let amount = get_basin_size(&low_point, &grid);
    //     println!("Amount: {}", amount);
    // }

    let mut sum_2: Vec<usize> = low_points.iter().map(
        |low_point| 
            get_basin_size(low_point,&grid)
        ).collect();

    sum_2.sort();

    let sum_2: usize = sum_2.into_iter().rev().take(3).reduce(|acc, c| acc * c).unwrap(); 
    
    println!("Array:\n{:?}",sum_2);

}

fn check_neighbors(grid: &Vec<Vec<usize>>,row: usize,col: usize) -> bool{
    let height = grid.len();
    let width = grid[0].len();
    let val = grid[row][col];
    let irow = row as isize;
    let icol = col as isize;
    (!check_inbounds(irow-1, icol  , height, width) || val < grid[row-1][col]) &&
    (!check_inbounds(irow  , icol-1, height, width) || val < grid[row][col-1]) &&
    (!check_inbounds(irow+1, icol  , height, width) || val < grid[row+1][col]) &&
    (!check_inbounds(irow  , icol+1, height, width) || val < grid[row][col+1]) 
}

fn check_inbounds(row: isize, col:isize, height:usize, width:usize) -> bool {
    check_bound(row,height) && check_bound(col,width)
}
fn check_bound(index:isize, space: usize) -> bool {
    index >= 0 && index < space.try_into().unwrap()
}

fn get_basin_size(point: &Point, grid: &Vec<Vec<usize>>) -> usize {
    get_basin_points(point, grid).len()
}

fn get_basin_points(point: &Point, grid: &Vec<Vec<usize>> ) -> Vec<Point>{
    let mut stack: Vec<Point> = Vec::new();
    let mut checked: Vec<Point> = Vec::new();
    stack.push(*point);
    while !stack.is_empty() {
        let p = stack.pop().unwrap();
        //println!{"{:?}",p};
        if check_inbounds(p.row as isize, p.col as isize, grid.len(), grid[0].len()) &&
                grid[p.row][p.col] != 9 && !can_find(&checked, &p) {
            checked.push(p);
            stack.push(Point{ row: p.row+1, col: p.col   });
            stack.push(Point{ row: p.row,   col: p.col+1 });
            if p.row > 0 { stack.push(Point{ row: p.row-1,  col: p.col   }); }
            if p.col > 0 { stack.push(Point{ row: p.row,   col: p.col-1 }); }
        }
    }
    checked
}

fn can_find(vec: &Vec<Point>, point: &Point) -> bool {
    vec.iter().position(|p| p.row == point.row && p.col == point.col) != None
}

fn open_and_parse_lines(filename: &str) -> Vec<String> {
    let f = File::open(filename).expect("Problem happened when openning file");
    let reader = BufReader::new(f);

    reader.lines().map(|x| x.unwrap()).collect()
}