macro_rules! max{
    ($x:expr, $y:expr) => {
        if $x >= $y {
            $x
        } else {
            $y
        }

    }
}

fn main() { 
    let x = 10;
    let y = 20;
    let z = max!(x, y);
    println!("{}",z);
}
