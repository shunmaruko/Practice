///関数の確認
fn main(){
    println!("call original function.");
    my_func();
    println!("finished original function.");
    let result: f64 = cal_add(10.0, 3.987);
    println!("{}", result);
    let (x, y) = exchange(10., 5.);
    println!("{} {}", x, y);
    let result = factorial(10);
    println!("{}", result);
}

fn my_func(){
    println!("Hello World!");
}

///have arguments
fn cal_add(x: f64, y: f64) -> f64{
    let z: f64  = x * y;
    return z;
}

///multi return
fn exchange(x: f64, y: f64) -> (f64, f64){
   return (y, x);
}

///recursive function
fn factorial(n: i32) -> i32{
    if n == 1{
        return 1;
    } else {
        factorial(n-1) * n
    }
}

