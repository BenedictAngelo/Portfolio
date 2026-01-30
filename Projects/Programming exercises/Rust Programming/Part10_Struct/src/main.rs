struct GroceryItem{
    stock: i32,
    price: f64,
}
fn main() {
    let cereal = GroceryItem{
        stock: 10,
        price: 3.99,
    };
    let currency = "$";
    println!("The stock is: {}",cereal.stock);
    println!("The price is: {}{}",cereal.price,currency);
}
