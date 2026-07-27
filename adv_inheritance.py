# Single or basic inheritance

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# class Child(A):
#     def play(self):
#         print(f"{self.name} is playing")


# child = Child("Alice")
# child.greet()
# child.play()

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


# Multilevel Inheritance

# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#          print(f"{self.name} tells a story.")


# class A(Grandparent):
#     def work (self):
#         print(f"{self.name} is working")


# class Child(A):
#     def play(self):
#         print(f"{self.name} is playing")


# child = Child("Sam")
# child.tell_story()
# child.work()
# child.play()

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# Hierarchical Inheritance

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class B(A):
#     def play(self):
#         print(f"{self.name} is playing")

# class C(A):
#     def study(self):
#         print(f"{self.name} is studying")


# B = B("Dave")
# C = C("Eve")

# B.greet()
# B.play()

# C.greet()
# C.study()


#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


# Multiple

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}")

# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}")
#         super().greet()



# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}")
#         super().greet()

# class D(B, C):
#     def greet(self):
#         print(f"Hello from D, {self.name}")
#         super().greet()

# d = D("Frank")
# d.greet()



#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


# Hybrid

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")


class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")


class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  #Explicitly calling the constructor


    def nocturnal(self):
        print(f"{self.name} is nocturnal")

bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()