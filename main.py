class Dog:
    # Class variable
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def display_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}"

# Creating instances of Dog for two different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Displaying details of each dog
print(dog1.display_details())
print(dog2.display_details())
