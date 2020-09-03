# object_oriented.py
"""Python Essentials: Object Oriented Programming.
<Name>
<Class>
<Date>
"""


class Backpack:
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color, max_size = 5):
        """Set the name and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
        """
        self.name = name
        self.contents = []
        self.max_size = max_size

    def put(self, item):
        """Add an item to the backpack's list of contents."""
        self.item = item
        
        if len(self.contents) < self.max_size :
            self.contents.append(self.item)
        else :
            print("No room!")
            
    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)
        
    def dump(self):
        self.contents = []
        

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        return len(self.contents) + len(other.contents)
        """Add the number of contents of each Backpack."""
    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)


# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):

    def __init__(self, name, color, max_size = 2,  fuel = 10):
        """Set the name and initialize an empty list of contents."""
        Backpack.__init__(self, name, color, max_size = 2)
        self.fuel = fuel

    """Accepts an amount of fuel to be burned and decrements the
    fuel attribute by that amount. """
    def fly(self, fuel_ammount):
        self.fuel_ammount = fuel_ammount
        self.fuel -= self.fuel_ammount
        if self.fuel_ammount > self.fuel:
            print("No fuel! You die :p")
        else :
            print("Alive for now :D")
     
    def dump(self):
        Backpack.dump(self)
        self.fuel = 0
        
# Problem 4: Write a 'ComplexNumber' class.
def test_pack():
    testpack = Backpack("Barry", "black") # Instantiate the object.
    if testpack.name != "Barry": # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer", "foo", "bar"]:
        testpack.put(item) # Test a method.
        print("Contents:", testpack.contents)
    testpack.dump()
    print(testpack.contents)
    testpack_2 = Jetpack("Jojo", "green",)
    for item in ["pencil", "pen"]:
        testpack.put(item) # Test a method.
        print("Contents:", testpack.contents, "Status:", testpack_2.fly(11))
        testpack.dump()
        print(testpack.contents)
if __name__ == "__main__":
    test_pack()
