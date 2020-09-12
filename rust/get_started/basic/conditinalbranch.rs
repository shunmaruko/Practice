///Explore conditional bramch
fn main(){
    //if
    let x = 80;
    let mut flag: bool = true;
    if flag {
        println!("you are OK! score {}", x);
    } else { 
        println!("you need to try again.");
    }
    flag = false;
    if flag {
        println!("you are OK! score {}", x);
    } else { 
        println!("you need to try again.");
    }

    if x > 80 {
        println!("Grade A, Score:{}", x); 
    } else if x > 60 {
        println!("Grade B, Score:{}", x); 
    } else if x > 40 {
        println!("Grade C, Score:{}", x); 
    } else if x > 20 {
        println!("Grade D, Score:{}", x); 
    } else {
        println!("Grade D, Score:{}", x); 
    } 
    //loop
    // i is mutable variable
    for i in 0..10{
        println!("{}", i);
    }
    //nested loop
    for i in 0..10{
        for j in 0..10{
            println!("{}",i*j);
        }
    }
    //wihle loop
    //you need to declare the variable 
    let mut i = 0;
    while i < 10{
        println!("{}", i);
        i += 1;
    }
    //infinity loop
    i = 0;
    loop {
        println!("{}", i);
        i += 1;
        if i > 100 {
            break;
        }
    }
}
