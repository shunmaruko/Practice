struct Cube {
    width: i32,
    height: i32,
    depth: i32,
}
impl Cube {
    //constructer
    fn new(width: i32, height: i32, depth: i32) -> Cube{
        Cube{width: width, height: height, depth: depth}
    }

    //static method
    fn get_num_surface() -> i32 {
        6
    }

    fn get_volume(&self) -> i32{
        self.width * self.height * self.depth
    }

    fn get_area(&self) -> i32 {
        self.width * self.height * 2 + self.height * self.depth * 2 + self.depth * self.width *2
    }
}

fn main() {
    let cube = Cube::new(10, 20, 50);
    println!("length of cube ({}, {}, {})", cube.width, cube.height, cube.depth);
    println!("Volume of cube : {}", cube.get_volume());
    println!("Surface of cube : {}", cube.get_area());
    println!("number of surface : {}", Cube::get_num_surface());
}
