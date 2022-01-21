from game.card import Card

class Director:
    """A director, whose responsibility is to keep the 
    game going
    
    Attributes:

    
    """

    def __init__(self):
        """Constructor for our Director
        
        Args:
            self (Director): an instance of Director
        """
        self.card = None
        self.next_card = None
        self.score = 300
        self.is_playing = True
        self.choice = ""
        

    def start_game(self):
        """Start the game by running the main game loop
        
        Args:
            self (Director): an instance of Director
        """
        
        print("\nWelcome to High Low game.")
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        
    def get_inputs(self):
        """Show one card and asks the the user to guess if the 
        next card is higher or lower
        
        Args:
            self (Director): an instance of Director
        """
    
        # If it's not the first game iteration, we 
        # should assign our last card to our self.card here.
        if self.card == None:
            self.card = Card()
        else:
            self.card = self.next_card
    
        print("\nThe card is: {self.card.value}")
        self.choice = input("Higher or lower? [h/l] ")
        
    def do_updates(self):
        pass
        