fn main(){
    let mut  x: i32  = 100;
    let z: f64  = 50.0;
    let y: i32  = 50;
    //raw pointer & constant
    let iadress: *const i32 = &x; 
    //参照外し（ポインタが指すアドレスに格納されている値にアクセス)をおこなう際には明治的にunsafeブロックつかう
    unsafe{
        println!("value of variable at iadress : {}", *iadress); //reference
    }
    println!("value of iadress : {:?}", iadress); //{:?} is format for address
    //raw pointer & mutable variable
    let id: *mut i32 = &mut x; 
    unsafe{
        println!("before change id:{:?} x:{}", id, *id);
        *id = 30;
        println!("before change id:{:?} x:{}", id, *id);
    }
    //mutable pointer & mutable variable
    let mut iid: *const i32 = &x;
    let fid: *const f64 = &z;
    unsafe{
        println!("before change id:{:?} x:{}", iid, *iid);
        *id = 30;
        println!("before change id:{:?} x:{}", iid, *iid);
    }
    iid = &y;
    println!("before change id:{:?}", iid);
    println!("before change id:{:?}", fid);
}

