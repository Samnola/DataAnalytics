# Restaurant Class exercise 

class Restaurant:
    """This class stores restaurant information."""
    def __init__ (self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        rating = int(input(
            "How would you rate your experience today on a scale of 1-5? " \
        ))

        self.customer_ratins.append(rating)

        average = sum(self.customer_ratings) / len(self.customer_ratings)

        print(f"Your rating was {rating}.")
        print(f"The average rating for this restaurant is {average:.2f}")
    
    # create restaurant objects
restaurant1 = Restaurant("Burger King", "Burgers")
restauran2 = Restaurant("Taco Bell", "Mexican")
restaurant3 = Restaurant("Olive Garden", "Italian")

#test method
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()

