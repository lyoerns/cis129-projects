#CIS129_LeeYoerns_Lab12
#private: name, type, age
    #use decorators
#inputs: enter pet name, pet age, pet type


class Pet:
    """Class Pet with read-write properties"""
    def __init__(self, name, type, age):
        """Initialize Pet objects"""
        self.name = name
        self.type = type
        self.age = age
    
    @property
    def name(self):
        """return pet name"""
        return self._name
    @name.setter
    def name(self, name):
        """Set pet name"""
        self._name = name
    @property
    def type(self):
        """return pet type"""
        return self._type
    @type.setter
    def type(self, type):
        """Set pet type"""
        if not type.isalpha():
            raise ValueError(type, "is not a type of animal!")
        self._type = type
    @property
    def age(self):
        """return pet age"""
        return self._age
    @age.setter
    def age(self, age):
        """Set pet age"""
        if not age.isnumeric(): #makes sure age is a number
            raise ValueError("Age must be a positive number")
        self._age = age

#main

#input values:
input_name = input("Enter your pet's name: ")
input_type = input("Enter the animal your pet is: ")
input_age = input("Enter the age of your pet in years: ")

#create object of class Pet:
animal = Pet(input_name, input_type, input_age)

#display values:
print("The pet's name is", animal.name)
print("The pet's type is", animal.type)
print("The pet's age is", animal.age)



