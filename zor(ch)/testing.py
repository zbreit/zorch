class Parent(object):
    def __init__(self, name = None, age = None, **kwargs):
        self.name = name
        self.age = age
        print("In Parent: ")
        for x in kwargs:
            print(x, kwargs[x])
        print("\n")
        
class Subclass(Parent):
    def __init__(self, description = None, **kwargs):
        super(Subclass, self).__init__(**kwargs)
        self.description = description
        print("In Subclass: ")
        
        for x in kwargs:
            print(x, ":", kwargs[x])
        
        
        print("\n")
        

zach = Subclass(description="Zach", name="A cool dude", age=80)
print(zach.age, zach.description, zach.name)
