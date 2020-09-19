fn reverse(pair: (i32, bool)) -> (bool, i32){
    let (integer, boolean) = pair;
    (boolean, integer)
}
fn main() {
    //variables need to be annotated
    let flag: bool = true;

    //Numbers is annotated not only type but also suffix
    let a_float: f64 = 1.0;
    let a_integer = 5i32;

    //or a deafault will be used
    let b_float = 3.0; //'f64'
    let b_integer = 5; //'i32'

    //A type can be inferred from other line
    let mut inferred_type = 12; //Mutable 'i64' is inferred from other line
    // in this case you need to declare type using suffix explicitly
    inferred_type = 4294967296i64; 
    println!("{}",inferred_type);

    //mutable varibale can be changed
    let mut mutable = 12;
    mutable = 21;

    //error type of variable cannot be changed
    //mutable = true;

    //variables can be overwritten with shadowing
    let mutable = true;
    //0b11111111 interpreted as 256u8, which raises error
    let x: i8 = 0b00001111;
    let y: u8 = 0b11111111;
    let z = -20i8;
    let z_2 = 20i8;
    println!("{:8b} {:8b}", z, z_2);
    println!("{} {}", x, y);
    let pair = reverse((20i32, true));
    println!("{:?}", reverse((20i32, true)));
}
