class Dice():
    """Class representing Die to be cast"""
    def __init__(self, sides):
        self.sides = 6
        if sides:
            self.sides = sides

    def roll_Die(self):
        from random import randint
        """Rolls the dice"""
        num = randint(1,self.sides)
        print(f'You rolled a {num}')

dice6 = Dice(6)
dice6.roll_Die()
dice10 = Dice(10)
dice10.roll_Die()
dice20 = Dice(20)
dice20.roll_Die()
