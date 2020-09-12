fn main() {
    let msg: String = String::from("Hello world!");
    let name = "My name is Alice.".to_string();
    let adress: &str = "666-3333";
    let id: *const &str = &adress;
    println!("{:?}", id);
    println!("{}", msg);
    println!("{}", name);
    println!("{}", adress);
    //connect string 
    let mut mes = String::new();
    mes.push_str("Hello");
    //''str " "char type 
    mes.push(' ');
    mes.push_str("world!");
    println!("{}", mes);
}
