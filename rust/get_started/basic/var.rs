//global variable
static PI: f64 = 3.14159265;

fn get_cir(radius: f64) -> f64{
    2.0 * PI * radius
}
fn get_area(radius: f64) -> f64{
    PI * radius * radius
}

fn main(){
    let radius = 10.0;
    let cir = get_cir(radius);
    let area = get_area(radius);
    println!("{}, {}", cir, area);
}
