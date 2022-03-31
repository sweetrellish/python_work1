from UniversityAthletics import *

athletics = UniversityAthletics('Salisbury University', 'Baseball')
basketball = Basketball('Salisbury University', 'Basketball')
print(athletics.university_name)
print(athletics.sport)

athletics.describe_athletics()
athletics.in_season()

print(f'The athletic team sold {athletics.tickets_sold} tickets.')
athletics.tickets_sold = 100
print(f'The athletic team sold {athletics.tickets_sold} tickets.')
athletics.set_tickets_sold(50)
print(athletics.tickets_sold)
athletics.increment_tickets_sold(50)
print(athletics.tickets_sold)

print(basketball.get_genders('Male'))