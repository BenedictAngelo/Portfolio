fn greetings(time:i32){
    if time >= 10{
        println!("Hello");
    } 
    else{
        println!("Goodbye");
    }
}

fn main(){
    let time = 10;
    greetings(time);

    //----OR------
    let my_bool = true;
    if my_bool == true{
        println!("Hello");
    }else{
        println!("Goodbye");
    }
}
