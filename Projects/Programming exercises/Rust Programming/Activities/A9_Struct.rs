enum Flavor{
    Sprite,
    Melon,
    Chocolate,
}
struct Drinks{
    flavor: Flavor,
    fluid_oz: f64
}
fn print_drink(drink: Drinks){
    match drink.flavor{
        Flavor::Sprite => println!("The flavor is sprite"),
        Flavor::Melon => println!("The flavor is melon"),
        Flavor::Chocolate => println!("The flavor is Chocolate"),
    }
    println!("oz: {}", drink.fluid_oz);
}
fn main() {
    let sprite = Drinks{
        flavor:Flavor::Sprite,
        fluid_oz: 6.0
    };
    print_drink(sprite);
    let melon = Drinks{
        flavor:Flavor::Melon,
        fluid_oz: 7.0
    };
    print_drink(melon);
    let chocolate = Drinks{
        flavor:Flavor::Chocolate,
        fluid_oz: 5.0
    };
    print_drink(chocolate);
}
