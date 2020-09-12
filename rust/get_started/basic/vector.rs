///vector (allocatable array)
fn main() { 
    let mut vec: Vec(f64) = Vec::new();
    vec.push(1.2);
    vec.push(3.2);
    vec.push(4.4);
    println!("length of vector = {}", vec.len());
    println!("each value {:?}", vec);
    println!("vec[1] = {:?}", vev.get(1));
    println!("vec[1] = {}", vec.get(1).unwrap());
}
