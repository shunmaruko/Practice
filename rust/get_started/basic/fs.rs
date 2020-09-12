///try file io 
use std::fs;
fn main(){
    let s = fs::read_to_string("input1.txt").unwrap();
    println!("content of file \n {}", s);
}
