///vector (allocatable array)
fn main() { 
    let mut vec: Vec<f64> = Vec::new();
    vec.push(1.2);
    vec.push(3.2);
    vec.push(4.4);
    println!("length of vector = {}", vec.len());
    println!("each value {:?}", vec);
    //returns option type
    println!("vec[1] = {:?}", vec.get(1));
    //if get returns None, error happens
    println!("vec[1] = {}", vec.get(1).unwrap());
    //initialize vector with macro
    /*
    vec! macro equals to the following command
    let mut vec: Vec<i32> = Vec::new();
    vec.push(1);
    vec.push(3);
    vec.push(5);
    vec.push(7);
    vec.push(9);
     */
    let mut vec2: Vec<i32> = vec![1, 3, 5, 7, 9];
    for i in 0..5 {
        vec2[i] = vec2[i] * 2;
    }
    println!("{:?}", vec2);
}
