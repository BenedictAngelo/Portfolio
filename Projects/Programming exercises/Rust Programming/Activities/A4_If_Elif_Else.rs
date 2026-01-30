fn determine(a:i32){
    if a == 5{
        println!("It is equal to 5");
    }
    else if a >= 5{
        println!("It is more than 5");
    }
    else if a <= 5{
        println!("It is less than 5");
    }
    else{
        println!("Invalid");
    }
}

fn main(){
    let a = 10;
    determine(a);
}
