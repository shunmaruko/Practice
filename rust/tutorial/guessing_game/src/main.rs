use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");
    let secret_number: u32 = rand::thread_rng().gen_range(1, 101);
    //lower number is inclusive, though upper nunber is exclusive
    println!("The answer {}", secret_number);
    loop{
        println!("Please input your guess.");
        let mut guess = String::new();
        let ptr: *const String = &guess;//pointer for constant
        println!("ptr = {:?}", ptr);
        io::stdin()
            .read_line(&mut guess) //mutable reference
            .expect("Failed to read line"); //if io::Result is an Err value, raise message
        //shadowing variable(reuse)
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
            };
        //let ptr: *const u32 = &guess;//pointer for constant
        //println!("ptr = {:?}", ptr);
        println!("you guessed: {}", guess);
        match guess.cmp(&secret_number) {//it returns Less or Greater or Equal
            Ordering::Less => println!("Too small"),
            Ordering::Greater => println!("Too big"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }


}
