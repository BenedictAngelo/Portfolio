fn add(a:i32,b:i32)->i32 {
    a + b
}

fn result(){
    let x = add(5,19);
    println!("{x}");
   
}

//------OR---------

fn sum(c:i32, d:i32)->i32{
    c + d
}

fn display_result(outcome:i32){
    println!("{outcome:?}");
}

fn main(){
    result();
    let outcome = sum(5,19);
    display_result(outcome);
}
