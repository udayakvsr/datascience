#1
class Restaurant:
    def __init__(self, name, cuisine, address):
        self.name = name
        self.cuisine = cuisine
        self.address = address
#2
class Restaurant:
    def __init__(self, name, cuisine, address):
        self.name = name
        self.cuisine = cuisine
        self.address = address
    
    def __str__(self):
        return "This is a restaurant named {} serving {} dishes located at {}".format(self.name, self.cuisine, self.address)
#3
jersey_city = Restaurant("Satis Bistro", "European", "212 Washington St, Jersey City, NJ 07311")
print(jersey_city)
#4
class FastFood(Restaurant):
    def __init__(self, name, cuisine, address, drive_thru):
        super().__init__(name, cuisine, address)
        self.drive_thru = drive_thru

    def __str__(self):
        drive_thru_chk = "drive-thru" if self.drive_thru else "Not drive-thru"
        return "This is a fast food restaurant named {} serving {} dishes located at {} {}".format(
            self.name, self.cuisine, self.address, drive_thru_chk)
#5
starbucks = FastFood("Starbucks", "Coffee", "2641 John F. Kennedy Blvd, Jersey City, NJ 07306", True)
print(starbucks)
