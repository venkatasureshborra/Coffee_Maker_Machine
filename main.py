from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on=True
c= CoffeeMaker()
m = Menu()
mm=MoneyMachine()
while is_on:
    choice=input(f" enter your liked item{m.get_items()} : ").lower()
    if  choice=="off":
        is_on=False
    elif choice=="report":
        c.report()
        mm.report()
    else:
        drink =m.find_drink(choice)
        if  c.is_resource_sufficient(drink) and  mm.make_payment(drink.cost):
            c.make_coffee(drink)









