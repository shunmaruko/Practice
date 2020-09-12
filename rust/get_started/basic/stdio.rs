///practice standard io & parser
use std::io;
fn main(){
    println!("1:Name, 2:English, 3:Math, 4:Physics");
    //read string from standart input
    let mut line = String::new();
    io::stdin().read_line(&mut line).ok();

    //split by space
    let strs: Vec<&str> = line.split_whitespace().collect();
    let name = strs[0];
    let english: i32 = strs[1].parse().unwrap();
    let math: i32 = strs[2].parse().unwrap();
    let physics: i32 = strs[3].parse().unwrap();
    let sum: i32 = english + math + physics;
    println!("Score of {} : {}", name, sum);
}
