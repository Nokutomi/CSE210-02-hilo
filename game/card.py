from random import randint

class Card:
    
    def __init__(self) -> None:
        self.value = randint(1,13)
    
        