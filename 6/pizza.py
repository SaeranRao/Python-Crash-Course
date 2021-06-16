pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the fllowing toppings:")
for topping in pizza['toppings']:
    print(topping)