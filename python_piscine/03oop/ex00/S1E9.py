from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool) -> None:
        pass

    @abstractmethod
    def die(cls):
        pass


class Stark(Character):
    """class docstring"""
    
    def __init__(self, first_name :str, is_alive = True) -> None:
        """constructor docstring"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(cls):
        """method docstring"""
        cls.is_alive = False

    

Ned = Stark("Ned")
# hodor = Character("Hodor")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
