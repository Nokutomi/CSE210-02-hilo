from game.card import Card

class Director:
    """A director, whose responsibility is to keep the 
    game going
    
    Attributes:
        card (Card): The current card that will be asked upon.
        next_card (Card): The next card that will be used to evaluate
        score (int): The score for the entire game.
        is_playing (boolean): Whether or not the game is being played.
        choice (string): The current choice ('l' for lower, and 'h' for higher).
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

        # Shows at the end of the game
        print("\nThanks for playing.\n")
        
        
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
    
        self.choice = ""
        print(f"\nThe card is: {self.card.value}")
        while not self.choice in ("l", "h"):
            self.choice = input("Higher or lower? [h/l] ")
        
    def do_updates(self):
        """Make all the calculations for the game, assessing the choice of
        the player and the cards dealt.
        
        Args:
            self (Director): an instance of Director
        """
        self.next_card = Card()

        card = self.card.value
        next_card = self.next_card.value

        if card < next_card:
            if self.choice == "h":
                self.score += 100
            elif self.choice == "l":
                self.score -= 75
        elif card > next_card:
            if self.choice == "l":
                self.score += 100
            elif self.choice == "h":
                self.score -= 75
        elif card == next_card:
            print("The cards are equal in value. Score not changed")

    def do_outputs(self):
        """Displays the next card and the current score. Later, it asks whether
        the player wants to keep playing.
        
        Args:
            self (Director): an instance of Director
        """
        print(f"The next card was: {self.next_card.value}")
        print(f"Your score is: {self.score}")

        keep_playing = ""
        while not keep_playing in ("y", "n"):
            keep_playing = input(f"Play again [y/n]: ")

        if keep_playing == "n":
            self.is_playing = False
       
        