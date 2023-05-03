class Bird:
    def set_name(self,name):
        print("name is"+name)
    def is_fly(self, canFly):
        if canFly:
            print("I can fly")
        else:
            print("I can't fly")

def set_name_function(name):
    print("name is "+name)
    return name
a = "Peter"
duck = Bird()
duck.set_name("duck 1")
duck.is_fly(False)
c = set_name_function(a)
print(c)