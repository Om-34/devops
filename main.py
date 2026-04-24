n = int(input("Enter number of items: "))

# empty lists
values = []
weights = []

for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter capacity of knapsack: "))

#list to store ratio, value, weight
items = []
for i in range(n):
    ratio = values[i] / weights[i]
    items.append((ratio, values[i], weights[i]))

items.sort(reverse=True)

total_value = 0.0

for ratio, value, weight in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        fraction = capacity / weight
        total_value += value * fraction
        break

print("Maximum value:", total_value)