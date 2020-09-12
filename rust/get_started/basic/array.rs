fn main(){
    //if not designated shape and dtype of array, estimated by initail value
    let array = [2, 4, 6, 8, 10];
    //declare shape data type explicitly
    let starray: [f64;5] = [2.3, 4., 6.8, 8.7, 10.5];
    //initialize with a certain value
    const N: usize = 10;
    let mut array2 = [0; N];
    for i in 0..N {
        array2[i] = i * 10;
    }
    for i in 0..N {
        println!("array[{}] = {}", i, array2[i]);
    }
    for i in 0..5 {
        println!("array[{}] = {}", i, array[i]);
    }
    for i in 0..5 {
        println!("starray[{}] = {}", i, starray[i]);
    }
}
