class Dog():
    def __init__(self, color, age, breed):
        self.color = color
        self.age = age
        self.breed = breed
    def run(self):
        print("I can run")
    def eat(self):
        print("I can eat")

Charlie = Dog("Red", 20, "German")
print(Charlie.color)
Charlie.run()

Cooper = Dog("Light-brown", 15, "Bulldog")
print(Cooper.color)
Cooper.run()
