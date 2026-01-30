#[derive(Debug)]
enum Color {
    Black,
    Blue,
}

fn main_color(color:Color){
    match color{
        Color::Black=>println!("It is Black"),
        Color::Blue=>println!("It is Blue"),
    }
}
fn main() {
    main_color(Color::Black);
}
