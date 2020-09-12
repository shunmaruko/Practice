///可変参照の借用
fn main(){
    let mut fib: Vec<i32> = vec![0, 1];
    let mut cnt = 0;
    while cnt < 10{
        add_element(&mut fib);
        cnt += 1;
    }
    println!("fib = {:?}", fib);
}

fn add_element(fib: &mut Vec<i32>){
    let len: usize  = fib.len();
    let x: i32 = fib[len - 2];
    let y: i32 = fib[len - 1];
    fib.push(x + y);

}
