from turtle import clear


class Parent:
    def __init__(self, name) -> None:
        self.name = name
        self.child = Child("Josef", self)

    def whoami(self):
        print("Hi, I'm the a Parent of", self.child.name, "and my name is", self.name)

class Child:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent

    def whoami(self):
        print("Hi, I'm the a Child of", self.parent.name, "and my name is", self.name)

    def changeParentName(self, name):
        print("Changed name of Parent to", name)
        self.parent.name = name


testParent = Parent("Bob")
testParent.whoami()
testParent.child.whoami()
print()
testParent.child.changeParentName("Alice")
print()
testParent.whoami()
testParent.child.whoami()
