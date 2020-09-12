///データ型をまとめる
fn main(){
  // literal
  let dec = 25;//10進数
  let bin = 0b110011;//2進数
  let oct = 0o141;//8進数
  let hex = 0x1a2;//16進数
  println!("Literal");
  println!("dec = {}", dec);
  println!("bin = {}", bin);
  println!("oct = {}", oct);
  println!("hex = {}", hex);
  //float
  let a: f64 = 10000.0;
  let b: f64 = 33.;
  let c = 2.5;//regarded as f64 by default 
  let x = a / b;
  let y = b / a;
  let z = a / c;
  println!("x = {}", x);
  println!("y = {}", y);
  println!("z = {}", z);
  //boolean
  let flag: bool = true;
  println!("flag = {}", flag);
  let c1: char = 'r';
  let c2: char = 't';
  println!("{} {}",c1,c2);
  //tuple
  //any type is ok as value
  let _tupple = (10, 25, '1', "sample");
  let p = (10, 25);
  let (_, val) = p;
  println!("{}", val);
}
