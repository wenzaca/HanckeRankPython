# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = 0.00
    tax = 0.00
    totalCost = 0.00
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    totalCost = tip+tax+meal_cost
    print(round(totalCost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)