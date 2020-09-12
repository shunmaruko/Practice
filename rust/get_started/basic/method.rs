fn main(){
    //static method
    let min = i8::min_value();
    let max = i8::max_value();
    println!("i8 : {first:} ~ {second:}",first=min, second=max);
    let x:i8 = 0b01110101;
    println!("{}", x);
    println!("{:b}", x);
    println!("{:b}", x.rotate_left(3));
}
