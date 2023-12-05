from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

while True:
    order = input("​What would you like? (espresso/latte/cappuccino/): ")

    if order == "off":
        break   

    if order == "report":
        my_coffee_maker.report()
        continue
    
    ordered_coffee = my_menu.find_drink(order)      

    if ordered_coffee == None:
        continue    

    if my_coffee_maker.is_resource_sufficient(ordered_coffee) == False:
        continue    

    if my_money_machine.make_payment(ordered_coffee.cost) == True:
        my_coffee_maker.make_coffee(ordered_coffee)


