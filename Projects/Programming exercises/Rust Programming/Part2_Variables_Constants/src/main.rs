fn main() {
    let mut x = 4; // implicit assignment cause it doesn't have a data type
                        // add 'mut' so it defines as mutable and can be changed
    println!("x is: {}", x);

    x = 5;

    println!("x is: {}", x);

    // or we can do this

    let y = 4;

    println!("y is: {}", y);

    {
        
        let y = 10;  // scoping, variable only stays like that inside the scope '{}'

        println!("y is: {}", y);
    }

    let y = 6; // redeclaration

    println!("y is: {}", y);

    let y = y + 2; // or just reuse the variable

    println!("y is: {}", y);

    let y = "Hello, World"; // or just reuse the variable

    println!("y is: {}", y);

    // ------------CONSTANTS--------------
    // are immutable and cannot be reassigned

    const SECONDS_IN_MINUTE: u32 = 60;  
    println!("Seconds in the minute is {}", SECONDS_IN_MINUTE);




}
