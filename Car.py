class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayInfo()


    def displayInfo(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

    def findTax(self):
        if self.price > 10000:
            self.tax == 0.15
        else:
            self.tax == 0.12
        return self
car_1 = Car(2000, "35mph", "Full", "15mpg")
car_2 = Car(2000, "5mph", "Not Full", "105mpg")
car_3 = Car(2000, "15mph", "Kind of Full", "95mpg")
car_4 = Car(2000, "25mph", "Full", "25mpg")
car_5 = Car(2000, "45mph", "Empty", "25mpg")
car_6 = Car(2000000, "35mph", "Empty", "15mpg")
    
