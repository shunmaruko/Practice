static GLOBAL: i32 = 99;

fn main(){
    let local: i32 = 10;
    let mut ptr: *const i32 = &local;//pointer for constant
    //acccesss to local through ptr
    unsafe{
        println!("{}", *ptr);
    }
    println!("ptr = {:?}", ptr);
    ptr = &GLOBAL;
    unsafe{
        println!("{}", *ptr);
    }
    println!("ptr = {:?}", ptr); 
}

