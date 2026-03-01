class Rocket: 
    
    def __init__(self, name, fuel_level):
        self.name = name
        self.fuel_level = fuel_level 

    def add_fuel(self,amount):
        self.fuel_level += amount
        print(f"Fuel added. Updated fuel level: {self.fuel_level}")
    def launch(self):
        if self.fuel_level>= 10:
            print("Rocket launched successfully!")
            self.fuel_level -= 10
        else:
            print("Error: Not enough fuel! Please add fuel.")

apollo = Rocket("Apollo11", 5)

apollo.launch()

apollo.add_fuel(10)

apollo.launch()

    
