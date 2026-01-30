enum Direction{
    Up,
    Down,
    Left,
    Right,
}
fn main() {
    let go = Direction::Left;
    match go{
        Direction::Up => println!("Go Up"),
        Direction::Down => println!("Go Down"),
        Direction::Left => println!("Go Left"),
        Direction::Right => println!("Go Right"),
    };
}
