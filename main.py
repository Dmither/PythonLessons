class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    is_admin = False
    level = None
    partner = None
    def __str__(self):
        return f"Person name: {self.name}, age: {self.age}"
    def merriage(husband, wife):
        if isinstance(husband, Person) and isinstance(wife, Person):
            husband.partner = wife
            wife.partner = husband

frank = Person("Frank", 36)
print(frank)
print(frank.is_admin)

class Admin(Person):
    is_admin = True
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

sam = Admin("Sam", 38, "first")
print(sam)
print(sam.is_admin)
print(sam.level)
print(frank.level)