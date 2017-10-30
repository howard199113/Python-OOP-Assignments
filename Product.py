class products(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    
    def addTax(self, tax):
        self.price *= (1+tax)
        return self
    
    def returnning(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "new":
            self.status = "for sale cheaper"
        elif reason == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    
    def displayInfo(self):
        print "price:", self.price
        print "item name:", self.item_name
        print "weight:", self.weight
        print "brand:", self.brand
        print "cost:", self.cost
        print "status:", self.status

    
product1 = products(10, "basketball", 3, "spalding", 7).returnning("defective").displayInfo()




