def home_wrecker(*item):
    """Accepts ingredients for burrito, 
    And prints everything in the burrito."""
    print("\nMaking a burrito with the ingredients:")
    for ingredient in item:
        print(f'- {ingredient}')

home_wrecker('Sour cream', 'Cheese', 'Beans')
home_wrecker('Chicken', 'Rice')
home_wrecker('Rice')