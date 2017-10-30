class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self
    
    def displayInfo(self):
        print "Health:", self.health



# a1 = Animal("cat", 50).walk().walk().walk().run().run().displayInfo()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
        
    def pet(self):
        self.health +=5
        return self

d = Dog("beagle", 50)
d.walk().walk().walk().run().run().pet().displayInfo()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 15
        return self
    
    def displayInfos(self):
        print self.health,"I am a Dragon"

d = Dragon("Dragon", 0)
d.fly().displayInfos()

    