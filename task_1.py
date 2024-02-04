from pulp import *

model = LpProblem("Maximize Production", LpMaximize)

lemonade = LpVariable("Lemonade_units", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_juice_units", lowBound=0, cat="Integer")

model += 2 * lemonade + fruit_juice <= 100
model += lemonade <= 50
model += lemonade <= 30
model += 2 * fruit_juice <= 40

model += lemonade + fruit_juice

model.solve()

print("Status:", LpStatus[model.status])
print("Maximum production:", value(model.objective))
print("Production of Lemonade:", int(lemonade.varValue))
print("Production of Fruit Juice:", int(fruit_juice.varValue))
