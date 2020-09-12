fn main() {
    let name = "Alice".to_string();
    introduce(&name);
    println!("{}", name);

}
fn introduce(myname: &String) {
    println!("My name is {}", myname);
}
