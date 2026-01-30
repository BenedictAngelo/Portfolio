fn check(a:bool){
    match a{
        true => println!("It is indeed true"),
        false => println!("It is indeed false"),
    }
}

fn counter(num:i32){
    match num{
        1 => println!("Its 1"),
        2 => println!("Its 2"),
        3 => println!("Its 3"),
        _ => println!("other"),
    }
}

fn main(){
    let a = true;
    check(a);
    let num = 1;
    counter(num);
}
