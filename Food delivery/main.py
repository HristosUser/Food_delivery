class Restaurant:
    def __init__(self, name, ID, address, location):
        self.name = name
        self.id = ID
        self.address = address
        self.location = location
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def delete_food(self, food_name):
      found = False
      for food in self.menu:
          if food.name == food_name:
              self.menu.remove(food)
              found = True

      if not found:
          print(f'Could not find {food_name} in menu')

class Food:
    def __init__(self, type, name, price, vegetarian, gluten_free):
        self.type = type
        self.name = name
        self.price = price
        self.vegetarian = vegetarian 
        self.gluten_free = gluten_free

def main():
    rest1 = Restaurant('Vairāk saules', 1, 'Domino shopping', (50.1234, 45.6787))

    rest1.add_food(Food('Starter', 'Springs rolls', 4.00, True, True))
    rest1.add_food(Food('Salad', 'Cezar', 8.00, False, True))
    rest1.add_food(Food('Main', 'Lazania', 5.00, False, True))

    rest1.delete_food('Lazania')

    print(len(rest1.menu))

main()