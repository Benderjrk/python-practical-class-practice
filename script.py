from datetime import time

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "The {name} menu is available from {start_time} to {end_time}".format(name=self.name,start_time=self.start_time,end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items.get(item)
    
    return total_price
    
# 11am to 4pm
brunch_menu = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}

# 3pm to 6pm
early_bird_menu = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}

# 5pm to 11pm
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}

# 11am to 9pm
kids_menu = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

arepas_menu = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}

brunch = Menu("brunch", brunch_menu, time(11), time(16))

early_bird = Menu("early bird", early_bird_menu, time(15), time(18))

dinner = Menu("dinner", dinner_menu, time(17), time(23))

kids = Menu("kids", kids_menu, time(11), time(21))

arepa = Menu("arepa", arepas_menu, time(10), time(20))
# print(brunch)

first_bill = brunch.calculate_bill(["pancakes", "home fries", "coffee"])

# print(first_bill)

second_bill = early_bird.calculate_bill(["mushroom ravioli (vegan)", "salumeria plate"])

# print(second_bill)

all_menus = {brunch, early_bird, dinner, kids, arepa}

franchise_addresses = {
  "west_end": "1232 West End Road",
  "east_mulberry": "12 East Mulberry Street"
}

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address

  def available_menus(self, the_time):
    available_menus = []
    asking_time = time(the_time)
    for menu in self.menus:
      menu_start = menu.start_time
      menu_end = menu.end_time
      if asking_time > menu_start and asking_time < menu_end:
        available_menus.append(menu)
    return available_menus
      
flagship_store = Franchise(franchise_addresses.get("west_end"), all_menus)
new_installment = Franchise(franchise_addresses.get("east_mulberry"), all_menus)

available_at_12 = flagship_store.available_menus(12)
available_at_5 = new_installment.available_menus(17)
# print("Flagship:", flagship_store)
# print("Second Store:", new_installment)
# print(available_at_12)
# print(available_at_5)

basta_franchises = [flagship_store, new_installment]
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



Business("Basta Fazoolin' with my Heart", basta_franchises)

arepas_place = "189 Fitzgerald Avenue"
Business("Take a' Arepa", arepas_place)

