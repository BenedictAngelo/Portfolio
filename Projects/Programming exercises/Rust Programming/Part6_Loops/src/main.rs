fn main() {
    let mut a = 0; // make it mutable
    loop{
        if a == 5{
            break;
        }

        println!("{a}");
        a = a + 1; // starts counting to 0 to 4
    }

    println!("================");

    //--------WHILE Loop------------
    let mut b = 5;
    while b != 10{ // while b is NOT EQUAL to 10
        println!("{b}");
        b = b + 1;
    }
}
