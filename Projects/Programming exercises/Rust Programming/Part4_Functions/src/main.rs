

fn first_name(){
    println!("Benedict Angelo");
}

fn last_name(){
    println!("Bumatay");
}



fn main() {
    
    first_name();
    last_name();




    fn add(a: i32, b:i32) -> i32 {
        a + b
    }

    let x = add(1,2);
    let y = add(3,4);
    let z = add(x,y);

    println!("{}",x); // '!' means using a macro instead of a function
    println!("{y}"); // variable can be typed directly inside the token like in python
    println!("{:?}",z); // '{:?}' means debug print
}
