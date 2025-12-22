# class --> keyword to define a new class
class Dog:

    # __init__ is a constructor
    # it runs every time an object is created
    def __init__(self, name, age):
        self.name = name   # name of the dog
        self.age = age     # age of the dog

    # behavior of the Dog class
    def bark(self):
        return f"{self.name} doesn't bark!"


# objects : instance of a class Dog
# dog1 is a Dog
# dog2 is a Dog
dog1 = Dog("Lucy", 4)
dog2 = Dog("test", 3)

# calling methods
dog1.bark()
dog2.bark()
