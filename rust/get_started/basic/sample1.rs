fn main(){
    //variable
    let x = 20;
    let y = 10;
    //variable
    let mut z ;
    //costant let name: type = value;
    //constはインライン化される
    let pi: i32 = 3;
    z = x + y;
    println!("{} + {}  = {}", x, y, z);
    z = x - y;
    println!("{} - {}  = {}", x, y, z);
    z = x * y;
    println!("{} * {}  = {}", x, y, z);
    z = x * pi;
    println!("{} * {}  = {}", x, pi, z);
}
