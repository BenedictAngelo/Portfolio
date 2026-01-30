fn main() {
    let a = 99;
    if a > 99 {
        println!("BIG number");
    } else {
        println!("small number");
    }

    // -------Nested If else---------
    let b = 250;
    if b > 50 {
        if b > 200 {
            println!("HUGE number");
        } else {
            println!("BIG number");
        }
    } else {
        println!("small number");
    }

    // -------else if---------
    let c = 200;
    if c > 50 {
        println!("Big number");
    } else if c > 100 {
        println!("HUGE number")
    } else {
        println!("small number")
    }
}
