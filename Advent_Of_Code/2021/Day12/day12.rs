// use std::io::BufReader;
// use std::io::prelude::*;
// use std::fs::File; 
use std::vec::Vec;
use std::collections::HashMap;

#[derive(Debug)]
struct Node {
    neighbors: Vec<Node>,
    name: String,
}

fn main() {
    // let lines = open_and_parse_file("input.txt");

    let lines: Vec<String> = vec![String::from("a-b"), String::from("c-b"), String::from("a-c")];

    // Return option, None if can't find start
    let start = create_graph(lines);
    println!("{:?}", start);
}

fn create_graph(lines: Vec<String>) -> HashMap<String, Node> {
    let mut nodes: HashMap<String, Node> = HashMap::new();

    for line in lines {
        let split_names: Vec<String> = line.split("-").map(|s| s.to_string()).collect();

        //returns a borrowed value
        let node1 = nodes.entry(split_names[0].clone()).or_insert( Node {neighbors: Vec::new(), name: split_names[0]} );
        let node2 = nodes.entry(split_names[1].clone()).or_insert( Node {neighbors: Vec::new(), name: split_names[1]} );
        node1.neighbors.push(*node2);
    }
    nodes
}

// fn open_and_parse_file(filename: &str) -> Vec<String>{
//     let file = File::open(filename).expect("Couldn't open file");
//     BufReader::new(file).lines().map(|line| line.unwrap()).collect()
// }