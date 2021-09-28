#9.1

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'Restauracja czynna 8-21')

restaurant = Restaurant('Sok Bar', 'Soki')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


#9.3

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

user = User('Jan', 'Kowalski')
user.describe_user()
user.greet_user()

