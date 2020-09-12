static GLOBAL: i32 = 100;

fn main(){
    let array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let x: i32 = 10;
    let id: *const i32 = &x; 
    let id_gl: *const i32 = &GLOBAL; 
    let first: &[i32] = &array[0..5];
    let second = &array[6..10];
    println!("first = {:?}", first);
    println!("second = {:?}", second);
    println!("{}, {:?}", x, id);
}
