///try box type. used for reference
fn main(){
    let b: Box<i32> = Box::new(10);
    println!("b = {}", b);
    //string
    let name: &str = "Alice";
    println!("My name is {}", name);
    println!("My name is {}", name.len());
    println!("My name is {}", name.to_uppercase());
    println!("UTF8 = {:?}", name.as_bytes());
}
