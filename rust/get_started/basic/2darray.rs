fn main() {
    const N: usize = 3;
    const M: usize = 5;
    let mut array = [[0; M]; N];
    for i in 0..N {
        for j in 0..M{
            array[i][j] = 10 * i + j + 1;
        }
    }
    for i in 0..N {
        for j in 0..M{
            println!("array[{}][{}] = {}", i, j, array[i][j]);
        }
    }
}
