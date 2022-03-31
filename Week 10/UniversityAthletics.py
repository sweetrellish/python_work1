"""Class creation of University Athletics and Basketball"""
class UniversityAthletics:
    """Stores Athletic information for University"""
    def __init__(self, university_name, sport):
        """Initialize name and sport"""
        self.university_name = university_name
        self.sport = sport
        self.tickets_sold = 0

    def describe_athletics(self):
        """Prints information"""
        print(self.university_name.title())
        print(self.sport.title())
    
    def in_season(self):
        """Prints statement that sport is in season"""
        print(f'{self.sport} is in season!')
    
    def set_tickets_sold(self, num):
        """Defines the number of tickets sold."""
        self.tickets_sold = num

    def increment_tickets_sold(self, add):
        """Adds number of tickets sold in an event"""
        self.tickets_sold += add

class Basketball(UniversityAthletics):
    """Represents Basketball in athletics"""
    def __init__(self, university_name, sport):
        super().__init__(university_name, sport)
        self.gender = ''
    
    def get_genders(self, gender):
        """Returns the genders in Basketball"""
        self.gender = gender
        print(self.gender)
    

# athletics = UniversityAthletics('Salisbury University', 'Baseball')
# basketball = Basketball('Salisbury University', 'Basketball')
# print(athletics.university_name)
# print(athletics.sport)

# athletics.describe_athletics()
# athletics.in_season()

# print(f'The athletic team sold {athletics.tickets_sold} tickets.')
# athletics.tickets_sold = 100
# print(f'The athletic team sold {athletics.tickets_sold} tickets.')
# athletics.set_tickets_sold(50)
# print(athletics.tickets_sold)
# athletics.increment_tickets_sold(50)
# print(athletics.tickets_sold)

# print(basketball.get_genders('Male'))