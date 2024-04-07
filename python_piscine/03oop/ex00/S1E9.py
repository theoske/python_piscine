from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, first_name: str, is_alive: bool) -> None:
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """class docstring"""
    
    def __init__(self, first_name :str, is_alive = True) -> None:
        """constructor docstring"""
        super().__init__(first_name, is_alive)

    def die(cls):
        """method docstring"""
        cls.is_alive = False

    

Ned = Stark("Ned")
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
