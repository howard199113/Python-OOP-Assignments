class MathDojo(object):
    def __init__(self):
        self.result = 0
        
    def add(self, *args):
        for obj in args:
            if type(obj) == list or type(obj) == tuple :
                for value in obj:
                    self.result += value
            elif type(obj) == int:
                self.result += obj
        return self

        for val in args:
            self.adding += val
        
        self.result += self.adding
        return self

    def subtract(self, *args):
        for obj in args:
            if type(obj) == list or type(obj) == tuple:
                for value in obj:
                    self.result -= value
            elif type(obj) == int:
                self.result -= obj
        return self

        self.result -= self.subtracting
        return self

    def display(self):
        print self.result
   
md = MathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).display()
