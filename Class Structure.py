# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
#     def login(self):
#         self.logged = True
#         print self.name + "is logged in."
#         return self

# new_user = User("Howard", "howard199113@hotmail.com")
# print new_user.email

class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "bike's price:", self.price, "maximum speed:", self.max_speed, "total miles:", self.miles
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self
bike_1 = Bike(1000, "20mph", 0).ride().ride().ride().reverse().displayInfo()
bike_2 = Bike(500, "15mph", 0).ride().ride().reverse().reverse().displayInfo()
bike_3 = Bike(800, "30mph", 0).reverse().reverse().reverse().displayInfo()