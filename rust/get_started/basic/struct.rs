///practice structure (like dictionary)
struct Point { 
    x: i32,
    y: i32,
}

fn main(){
    let p = Point{x: 10, y: 20};
    println!("(x,y) = ({}, {})", p.x, p.y);
}
