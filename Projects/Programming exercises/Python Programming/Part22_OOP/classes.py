class Car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the car {self.color} {self.model}")

    def stop(self):
        print(f"You stopped {self.color} {self.model}")
