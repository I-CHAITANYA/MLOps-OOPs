# SIMPLE INHERITANCE

#base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# #derived class
# class Dog(Animal):
    
#     def __init__(self):
#         self.behaviour = "Friendly"



#     def speak(self):
#         print(f"{self.name} barks. he is {self.behaviour} in nature.")


# # animal = Animal("Generic Animal")
# # animal.speak()  # Output: Generic Animal makes a sound.

# dog = Dog()
# dog.speak()  # Output: Buddy barks.



#super keyword - to call the parent class constructor and methods



class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

#derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}.")


# animal = Animal("Generic Animal")
# animal.speak()  # Output: Generic Animal makes a sound.

dog = Dog("Golden Retriever")
dog.speak()  # Output: Buddy barks. It is a Golden Retriever.
